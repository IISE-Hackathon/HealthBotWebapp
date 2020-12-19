from django.shortcuts import render, HttpResponse,redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegisterationForm

# rendering the landing screen

def landingScreen(request):
    return render(request,template_name = 'landingscreen.html')

def loginScreen(request):
    return render(request,template_name = 'login.html')

def registerScreen(request):
    if request.method == 'POST':
        register = RegisterationForm(request.POST)
        print(register.errors)
        if register.is_valid():
            user = register.save()
            login(request,user)
            
            return redirect('chatroom')
        else:
            userform = RegisterationForm()
            render(request,'register.html',{'userform': userform } )
    
    else:
        userform = RegisterationForm()
        return render(request,'register.html',{'userform': userform } )

    userform = RegisterationForm()
    return render(request,'register.html',{'userform': userform } )
    

@login_required
def chatroom(request):
    return render(request,template_name = 'chatroom.html')

