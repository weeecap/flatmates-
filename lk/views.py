from django.shortcuts import render


def profile(request):
    return render(request, 'lk/pages/profile.html')

def account(request):
    return render(request, 'lk/pages/account.html')
# Create your views here.
