from django.urls import path 

from . import views 

app_name = 'lk'

urlpatterns = [
    path('account', views.account, name='account'),
    path('profile', views.profile, name='profile')
]