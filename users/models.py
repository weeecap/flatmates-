from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    image = models.ImageField(upload_to='users_image', null=False, blank=True)
    tg = models.CharField(max_length=30,null=False,blank=True)



