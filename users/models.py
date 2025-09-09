from django.db import models



class Profile(models.Model):
    username = models.CharField(max_length=50, blank=True, null=False)
    telegram = models.CharField(max_length=120, blank=True, null=True)
    gender = models.CharField(max_length=20, blank=True, null=True)
    
    def __str__(self):
        return self.username


# Create your models here.
