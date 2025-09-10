from django.shortcuts import render

from users.forms import UserLoginForm

def login(request):
    return render(request, 'users/pages/login.html')

def registration(request):
    return render(request, 'users/pages/registration.html')
