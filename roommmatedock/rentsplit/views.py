from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import ProfileAuth, Expense
from messageboard.models import Message
from django.urls import reverse
from django.db.models import Q
from django.contrib import messages
from django.db import IntegrityError

from django.contrib.auth.models import User

# Create your views here.

@login_required(login_url = 'users:login')
def index(request):
    try:
        user = request.user
        profile = ProfileAuth.objects.get(users=user)
        user_profiles = user.profile.all()
        calculated_rents, owed_user = results(profile)
        all_mes = Message.objects.filter(profile=profile)
        
        unread_count = all_mes.exclude(users_read=user).count()

        return render(request, 'rentsplit/index.html', {
            'user_profiles': user_profiles,
            'calculated_rents': calculated_rents,
            'all_mes': all_mes,
            'unread_count': unread_count
        })
    except:
        user_profiles = None
        calculated_rents = None
        all_mes = None 
        unread_count = None
        return render(request, 'rentsplit/index.html', {
            'user_profiles': user_profiles,
            'calculated_rents': calculated_rents,
            'all_mes': all_mes,
            'unread_count': unread_count
        })
def user_profile(request, profile_name):
    user = request.user
    profile = user.profile.get(name=profile_name)
    profile_users = profile.users.all()
    profile_expenses = profile.expense_fr_profile.all()

    calculated_rents, owed_user = results(profile)

    return render(request, 'rentsplit/user-profile.html', {
        'profile': profile,
        'profile_users': profile_users,
        'current_user': user,
        'profile_expenses': profile_expenses,
        'calculated_rents': calculated_rents,
        'owed_user': owed_user,
    })

def create_profile(request):
    if request.method == 'POST':
        profile_name = request.POST['room-name']
        try:
            user_ids = request.POST.getlist('users[]')
            description = request.POST['description']
            users = User.objects.filter(username__in=user_ids)
            current_user = request.user

            if not users :
                messages.warning(request, 'One of the usernames you entered does not exist')
                return index(request)


            user_list = users

            user_qs = User.objects.filter(id__in = [u.id for u in user_list])

            all_users_qs = user_qs | User.objects.filter(pk=current_user.pk)

            created_profile = ProfileAuth.objects.create(
                name = profile_name,
                description = description
            )
            created_profile.save()
            created_profile.users.set(all_users_qs)


            return user_profile(request, profile_name)
        except:
            messages.warning(request, 'Uh Oh, something went wrong')
            return user_profile(request, profile_name)


def add_expense(request, profile_name):
    expense_user = request.user
    profile = expense_user.profile.get(name=profile_name)


    if request.method == 'POST':

        
        name = request.POST['name']
        amount = float(request.POST['amount'])
        expense_user = request.POST['expense-user']

        current_user = User.objects.get(username=expense_user)

        if amount <= 0:
            messages.warning(request, 'Your expense has to be greater than 0')
            return redirect('rentsplit:user-profile', profile_name=profile_name)

        try:
            created_expense = Expense.objects.create(
                name = name,
                amount = amount,
                user = current_user,
                profile = profile,
            )
            created_expense.save()

            messages.success(request, f'{name} added to expenses')
            return redirect('rentsplit:user-profile', profile_name=profile_name)
        
        except ValueError:
            messages.warning(request, 'Your expense has to be a number')
            return redirect('rentsplit:user-profile', profile_name=profile_name)
        except IntegrityError:
            messages.warning(request, 'This expense already exists')
            return redirect('rentsplit:user-profile', profile_name=profile_name)

def update_rent(request, profile_name):
    user = request.user
    profile = user.profile.get(name=profile_name)

    if request.method == 'POST':
        new_rent = float(request.POST['rent'])
        
        #If rent is negative
        if new_rent <= 0:
            messages.warning(request, 'Your rent has to be greater than 0')
            return redirect('rentsplit:user-profile', profile_name=profile_name)
        else:
            try:
                profile.rent = new_rent
                profile.save()
                messages.success(request, 'Your rent was updated')
                return redirect('rentsplit:user-profile', profile_name=profile_name)
            except ValueError:
                messages.warning(request, 'Your rent has to be a number')
                return redirect('rentsplit:user-profile', profile_name=profile_name)


def results(profile):
    profile_users = profile.users.all()


    #Generate Results
    #Create dictionary with username: expense amounts
    total_expense_dict = {}
    user_num = 0
    rent = profile.rent
    calculated_rents = {}

    #IF EXPENSES IN PROFILE
    for u in profile_users:
        if u.expense_fr_user.all():
            user_expense = Expense.objects.filter(user=u)
            total_expense_dict[u.username] = sum(e.amount for e in user_expense)
        else:
            user_expense = 0
            total_expense_dict[u.username] = user_expense            

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
        calculated_rents[us] = (rent / user_num) - ( 2 * (expense / user_num)) + (other_expenses / (user_num)) 

    user_owed = 0
    owed_user = {}
    for count, amount in calculated_rents.items():
        if amount < 0:
            user_owed += 1
    not_owed_user = user_owed - user_num
    if not_owed_user == 0:
        not_owed_user = user_owed
    for key, value in calculated_rents.items():
        if value < 0:
            amount_owed = (value) / (not_owed_user)
            owed_user[key] = amount_owed
            calculated_rents[key] = 0
            for oother_user, other_value in calculated_rents.items():
                if oother_user != key:
                    calculated_rents[oother_user] = other_value + (value / (user_num - 1))


    return calculated_rents, owed_user

def remove_expense(request, expense_name, profile_name):
    profile = request.user.profile.get(name=profile_name)
    if profile.expense_fr_profile.all():
        expense_to_delete = Expense.objects.get(name=expense_name, profile=profile)
        expense_to_delete.delete()
        messages.success(request, f'{expense_to_delete.name} was removed')
        return redirect('rentsplit:user-profile', profile_name=profile_name)

def add_user(request, profile_name):
    profile = ProfileAuth.objects.get(name=profile_name)
    new_user_id = request.POST['username']
    profile_users = profile.users.all()

    try:
        new_user = User.objects.get(username=new_user_id)

        if new_user in profile_users:
            messages.warning(request, f'{new_user_id} is already in {profile.name}')

        profile.users.add(new_user)

        return redirect('rentsplit:user-profile', profile_name=profile_name)
    
    except:
        messages.warning(request, 'There is no user that has this username')
        return redirect('rentsplit:user-profile', profile_name=profile_name)

def reset_profile(request, profile_name):
    profile = ProfileAuth.objects.get(name=profile_name)
    all_expenses = profile.expense_fr_profile.all()

    for expense in all_expenses:
        expense.delete()
    
    messages.success(request, f'{profile.name}\'s expenses have been reset')
    return redirect('rentsplit:user-profile', profile_name=profile_name)

def profile_settings(request, profile_name):
    profile = ProfileAuth.objects.get(name=profile_name)
    if request.method == 'POST':
        if profile.name == 'Tommy\'s intern office':
            messages.warning(request, 'Guest profile settings can\'t be edited')
        elif 'settings-name' in request.POST:
            profile.name = request.POST['settings-name']
        elif 'settings-description' in request.POST:
            profile.description = request.POST['settings-description']
        profile.save()

    context ={
        'profile': profile,
    }
    return render(request, 'rentsplit/settings.html', context)

def delete_profile(request, profile_name):
    profile = ProfileAuth.objects.get(name=profile_name)
    if profile.name == 'Tommy\'s intern office':
        messages.warning(request, 'Guest profile can\'t be deleted')
        return redirect('rentsplit:profile-settings', profile_name)

    profile.delete()
    return redirect('index')