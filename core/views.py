from django.shortcuts import render

def index(request):
    context = {
        'title': 'Flatmates Hub',
        'message': 'Добро пожаловать!'
    }
    return render(request, 'pages/index.html', context)

def login(request):
    return render(request, 'pages/login.html')

def register(request):
    return render(request, 'pages/register.html')

def dashboard(request):
    return render(request, 'pages/dashboard.html')