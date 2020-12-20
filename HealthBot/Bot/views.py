from django.shortcuts import render, HttpResponse,redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import RegisterationForm
from django.contrib import messages

# rendering the landing screen

def landingScreen(request):
    return render(request,template_name = 'landingscreen.html')

def loginScreen(request):
    if request.method == 'POST':
        user_name = request.POST.get('username')
        passwd = request.POST['password']
        user = authenticate(request, username =  user_name, password = passwd)
        print(user)
        if user is not None:
            login(request, user)
            return redirect('chatroom')
        else:
            error = "Your account not found Pls Sign up or Pls enter valid credentials" 
            return render(request, 'login.html', {'error': error } )
    else:
        return render(request,'login.html',{'error':""} )

    return render(request,'login.html',{'error':""} )


def registerScreen(request):
    if request.method == 'POST':
        register = RegisterationForm(request.POST)
        if register.is_valid():
            user = register.save(commit=False)
            user.set_password(register.cleaned_data['password'])
            user.save()
            login(request,user)
            return redirect('chatroom')
        else:
            userform = RegisterationForm()
            error = register.errors
            return render(request,'register.html',{'userform': userform, 'error': error } )
    
    else:
        userform = RegisterationForm()
        return render(request,'register.html',{'userform': userform,'error': "" } )

    userform = RegisterationForm()
    return render(request,'register.html',{'userform': userform ,'error': ""} )
    

@login_required
def chatroom(request):
    return render(request,template_name = 'chatroom.html')

