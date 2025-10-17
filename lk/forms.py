from django import forms
from django.contrib.auth.forms import UserChangeForm

from users.models import User


class UserProfileForm(UserChangeForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label='Имя пользователя')
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control', 'readonly':True}), label='Email')
    tg = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label='Telegram')

    class Meta:
        model = User
        fields = ('username', 'email', 'tg', 'image')