from django.shortcuts import render

def index(request):
    context = {
        'title': 'Flatmates Hub',
        'message': 'Добро пожаловать!'
    }
    return render(request, 'core/pages/index.html', context)

def dashboard(request):
    return render(request, 'core/pages/dashboard.html')