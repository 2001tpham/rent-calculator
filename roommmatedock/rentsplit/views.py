from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'rentsplit/index.html')

def guest_create_profile():
    pass