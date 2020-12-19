from django.shortcuts import render


# rendering the landing screen

def landingScreen(request):
    return render(request,template_name = 'landingscreen.html')

def loginScreen(request):
    return render(request,template_name = 'login.html')

def registerScreen(request):
    return render(request,template_name = 'register.html')

def chatroom(request):
    return render(request,template_name = 'chatroom.html')

