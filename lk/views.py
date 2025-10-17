from django.shortcuts import render
from lk.forms import UserProfileForm


def profile(request):
    form = UserProfileForm()
    context = {'title': 'Личный кабинет', 'form':form}
    return render(request, 'lk/pages/profile.html', context)

def account(request):
    return render(request, 'lk/pages/account.html')
