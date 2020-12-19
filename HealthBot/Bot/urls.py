from django.urls import path
from .views import landingScreen
from .views import loginScreen
from .views import registerScreen
from .views import chatroom

urlpatterns = [

    path('',landingScreen,name='landingscreen'),
    path('login/',loginScreen,name='loginscreen'),
    path('register/',registerScreen,name = 'registerscreen'),
    path('chatroom/',chatroom,name = 'chatroom')
    

]

