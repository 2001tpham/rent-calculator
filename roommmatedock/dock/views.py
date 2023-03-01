from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'dock/index.html')

def options(request):
    return render(request, 'dock/options.html')