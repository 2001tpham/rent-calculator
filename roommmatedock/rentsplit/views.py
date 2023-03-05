from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import ProfileAuth, Expense
from django.urls import reverse

from django.contrib.auth.models import User

# Create your views here.

@login_required(login_url = 'users:login')
def index(request):
    user = request.user

    user_profiles = user.profile.all()

    return render(request, 'rentsplit/index.html', {
        'user_profiles': user_profiles,
    })

def create_profile(request):
    if request.method == 'GET':
        return render(request, 'rentsplit/create-profile.html')
    
    elif request.method =='POST':
        name = request.POST['room-name']

        user_id = request.POST['users']
        users = User.objects.get(username= user_id)
        current_user = request.user
        
        user_list = [users, current_user]

        user_qs = User.objects.filter(id__in = [u.id for u in user_list])

        created_profile_auth = ProfileAuth.objects.create(
            name = name,
        )
        created_profile_auth.users.set(user_qs)
        created_profile_auth.save()

        return redirect(reverse('rentsplit:add-expense', kwargs={'profile_name': name}))

    return render(request, 'rentsplit/user-profile.html', {
        'room-name': name,
        'users': users,
    })

def user_profile(request, profile_name):
    user = request.user
    profile = user.profile.get(name=profile_name)
    profile_users = profile.users.all()
    profile_expenses = profile.expense_fr_profile.all()

    calculated_rents = results(profile)

    return render(request, 'rentsplit/user-profile.html', {
        'profile': profile,
        'profile_users': profile_users,
        'current_user': user,
        'profile_expenses': profile_expenses,
        'calculated_rents': calculated_rents,
    })

def add_expense(request, profile_name):
    expense_user = request.user
    profile = expense_user.profile.get(name=profile_name)
    profile_users = profile.users.all()
    profile_expenses = profile.expense_fr_profile.all()

    calculated_rents = results(profile)


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
        return redirect(reverse('rentsplit:add-expense', kwargs={'profile_name': profile_name}))

    return render(request, 'rentsplit/user-profile.html', {
        'room-name': profile.name,
        'profile_users': profile_users,
        'current_user': expense_user,
        'profile': profile,
        'profile_expenses': profile_expenses,
        'calculated_rents': calculated_rents
    })

def update_rent(request, profile_name):
    user = request.user
    profile = user.profile.get(name=profile_name)
    profile_users = profile.users.all()
    profile_expenses = profile.expense_fr_profile.all()

    if request.method == 'POST':

        calculated_rents = results(profile)


        profile.rent = request.POST['rent']
        profile.save()

    return render(request, 'rentsplit/user-profile.html', {
    'room-name': profile.name,
    'profile_users': profile_users,
    'current_user': user,
    'profile': profile,
    'profile_expenses': profile_expenses,
    'calculated_rents': calculated_rents
})

def results(profile):
    profile_users = profile.users.all()


    #Generate Results
    #Create dictionary with username: expense amounts
    total_expense_dict = {}
    user_num = 0
    rent = profile.rent
    calculated_rents = {}

    for u in profile_users:
        user_expense = Expense.objects.filter(user=u)
        total_expense_dict[u.username] = sum(e.amount for e in user_expense)

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

        calculated_rents[us] = (rent / 3) - expense + (other_expenses / (user_num - 1))

    return calculated_rents
