from django.contrib.auth.models import AbstractUser
from django.db import models




class BlogUser(AbstractUser):
    # additional fields 
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    secret_code = models.CharField(max_length=6, blank=True, null=True)


    def __str__(self):
        return self.username

