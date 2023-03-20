from django.shortcuts import render, redirect 
from django.contrib.auth.decorators import login_required
from rentsplit.models import ProfileAuth
from .models import Message, Reply
from django.contrib.auth.models import User
from django.contrib import messages
from django.db import IntegrityError




# Create your views here

@login_required(login_url='users:login')
def index(request, profile_name):
        profile = ProfileAuth.objects.get(name=profile_name)
        all_messages = profile.profile_message.all()

        context = {
            'all_messages': all_messages,
        }
        return render(request, 'messageboard/index.html', {
            'all_messages': all_messages,
            'profile': profile,
        })


def add_message(request, profile_name):
    try:
        profile = ProfileAuth.objects.get(name=profile_name)
        current_user = request.user
        
        created_message = Message.objects.create(
            sender = current_user,
            profile = profile,
            subject = request.POST['form-subject'],
            body = request.POST['form-body'],
        )
        created_message.save()

        return redirect('messageboard:index', profile_name)
    except IntegrityError:
        messages.warning(request, 'This message has already been created, try changing the message a little')
        return redirect('messageboard:index', profile_name)


def open_message(request, profile_name, date, sender, subject):
    message_profile = ProfileAuth.objects.get(name=profile_name)
    message_sender = User.objects.get(username=sender)

    mes = Message.objects.get(
        sender=message_sender,
        profile=message_profile,
        created_date=date,
        subject=subject,
    )
    
    replies = Reply.objects.filter(parent_message = mes)

    mes.users_read.add(request.user)

    
    
    context = {
        'mes': mes,
        'replies': replies,
        'profile': message_profile,
    }
    return render(request, 'messageboard/open-message.html', context)

def message_reply(request, profile_name, date, sender, subject):
    if request.method == 'POST':
        message_sender = User.objects.get(username=sender)
        reply_body = request.POST['form-reply']
        reply_profile = ProfileAuth.objects.get(name=profile_name)
        reply_message = Message.objects.get(
        sender=message_sender,
        profile=reply_profile,
        created_date=date,
        subject=subject,
        )

        created_reply = Reply.objects.create(
            user = request.user,
            body = reply_body,
            parent_message = reply_message,
        )
        created_reply.save()
        return redirect('messageboard:open-message', profile_name, date, sender, subject)
    
def delete_message(request, profile_name, date, sender, subject):
    message_sender = User.objects.get(username=sender)
    reply_profile = ProfileAuth.objects.get(name=profile_name)
    mes = Message.objects.get(
    sender=message_sender,
    profile=reply_profile,
    created_date=date,
    subject=subject,
        )    
    
    if reply_profile.name == 'Tommy\'s intern office':
        messages.warning(request, 'Guest account messages can\'t be deleted')
        return redirect('messageboard:index', profile_name=profile_name)
    else:    
        mes.delete()
        return redirect('messageboard:index', profile_name=profile_name)