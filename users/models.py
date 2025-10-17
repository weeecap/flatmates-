from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    image = models.ImageField(upload_to='users_image', null=False, blank=True)
    tg = models.CharField(max_length=30,null=True,blank=True, verbose_name='Telegram')
    date_of_birth = models.DateField(max_length=50, null=True,blank=True, verbose_name='Birth Date')



