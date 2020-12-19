from django.shortcuts import render
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

# rendering the landing screen

def landingScreen(request):
    return render(request,template_name = 'landingscreen.html')

def loginScreen(request):
    return render(request,template_name = 'login.html')

def registerScreen(request):
    return render(request,template_name = 'register.html')

@login_required
def chatroom(request):
    return render(request,template_name = 'chatroom.html')

