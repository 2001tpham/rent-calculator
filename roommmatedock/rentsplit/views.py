from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import ProfileAuth, Expense
from django.urls import reverse
from django.db.models import Q

from django.contrib.auth.models import User

# Create your views here.

@login_required(login_url = 'users:login')
def index(request):
    user = request.user

    user_profiles = user.profile.all()

    return render(request, 'rentsplit/index.html', {
        'user_profiles': user_profiles,
    })

def user_profile(request, profile_name):
    user = request.user
    profile = user.profile.get(name=profile_name)
    profile_users = profile.users.all()
    profile_expenses = profile.expense_fr_profile.all()

    if profile.expense_fr_profile.all():
        calculated_rents = results(profile)
    else:
        calculated_rents = {}
        for person in profile.users.all():
            calculated_rents[person.username] = 0

    return render(request, 'rentsplit/user-profile.html', {
        'profile': profile,
        'profile_users': profile_users,
        'current_user': user,
        'profile_expenses': profile_expenses,
        'calculated_rents': calculated_rents,
    })

def create_profile(request):
    if request.method == 'POST':
        profile_name = request.POST['room-name']
        user_ids = request.POST.getlist('users[]')
        users = User.objects.filter(username__in=user_ids)
        current_user = request.user

        user_list = users

        user_qs = User.objects.filter(id__in = [u.id for u in user_list])

        all_users_qs = user_qs | User.objects.filter(pk=current_user.pk)

        created_profile = ProfileAuth.objects.create(
            name = profile_name
        )
        created_profile.save()
        created_profile.users.set(all_users_qs)

        return user_profile(request, profile_name)


def add_expense(request, profile_name):
    expense_user = request.user
    profile = expense_user.profile.get(name=profile_name)


    if request.method == 'POST':

        
        name = request.POST['name']
        amount = request.POST['amount']
        expense_user = request.POST['expense-user']

        current_user = User.objects.get(username=expense_user)

        created_expense = Expense.objects.create(
            name = name,
            amount = amount,
            user = current_user,
            profile = profile,
        )
        created_expense.save()
        # return user_profile(request, profile_name)
        return redirect('rentsplit:user-profile', profile_name=profile_name)

def update_rent(request, profile_name):
    user = request.user
    profile = user.profile.get(name=profile_name)

    if request.method == 'POST':
        profile.rent = request.POST['rent']
        profile.save()

        return redirect('rentsplit:user-profile', profile_name=profile_name)

def results(profile):
    profile_users = profile.users.all()


    #Generate Results
    #Create dictionary with username: expense amounts
    total_expense_dict = {}
    user_num = 0
    rent = profile.rent
    calculated_rents = {}
    expenses_exist = False

    #IF EXPENSES IN PROFILE
    for u in profile_users:
        if u.expense_fr_user.all():
            user_expense = Expense.objects.filter(user=u)
            total_expense_dict[u.username] = sum(e.amount for e in user_expense)
            expenses_exist = True
        else:
            user_expense = 0
            total_expense_dict[u.username] = user_expense
            expenses_exist = False
            

        user_num += 1

    for us in total_expense_dict:
        expense = total_expense_dict[us]
        other_expenses = 0

        for other_user in total_expense_dict:
            if other_user == us:
                other_expenses += 0
            else:
                other_expenses += total_expense_dict[other_user]

        #Calculated rent for this user
        if expenses_exist == True:
            calculated_rents[us] = (rent / user_num) - expense + (other_expenses / (user_num - 1)) 
        else:
            calculated_rents[us] = rent / user_num





    return calculated_rents

def remove_expense(request, expense_name, profile_name):
    profile = request.user.profile.get(name=profile_name)
    if profile.expense_fr_profile.all():
        expense_to_delete = Expense.objects.get(name=expense_name, profile=profile)
        expense_to_delete.delete()
        return redirect('rentsplit:user-profile', profile_name=profile_name)

def add_user(request, profile_name):
    profile = ProfileAuth.objects.get(name=profile_name)
    new_user_id = request.POST['username']
    new_user = User.objects.get(username=new_user_id)

    profile.users.add(new_user)

    return redirect('rentsplit:user-profile', profile_name=profile_name)
