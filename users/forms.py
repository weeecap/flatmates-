from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from users.models import User

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': "form-control py-4" , 'placeholder':"Введите имя пользователя"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': "form-control py-4" , 'placeholder':"Введите пароль"}))


    class Meta:
        model = User 
        fields = ('username', 'password')

class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': "form-control py-4" , 'placeholder':"Введите никнейм"}))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': "form-control py-4" , 'placeholder':"example@mail.com"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': "form-control py-4" , 'placeholder':"Не менее 8 символов"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': "form-control py-4" , 'placeholder':"Повторите ваш пароль"}))
    

    class Meta:
        model = User
        fields = ( 'username', 'email', 'password1', 'password2')

class UserCompleteProfileForm(forms.ModelForm):
    tg = forms.CharField(widget=forms.TextInput({
        'class':"form-control", 'label':'Telegram username'}))
    date_of_birth = forms.DateField(widget=forms.DateInput({
        'class':"form-control", 'type':'date', 'label':'Дата рождения'}))
    class Meta:
        model = User
        fields = ('tg', 'date_of_birth')



 

