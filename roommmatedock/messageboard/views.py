from django.shortcuts import render, redirect 
from django.contrib.auth.decorators import login_required
from rentsplit.models import ProfileAuth
from .models import Message, Reply

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




