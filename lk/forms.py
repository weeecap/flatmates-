from django import forms
from django.contrib.auth.forms import UserChangeForm

from users.models import User


class UserProfileForm(UserChangeForm):

    class Meta:
        model = User 
        fields = ('username', 'email', 'tg', 'image')