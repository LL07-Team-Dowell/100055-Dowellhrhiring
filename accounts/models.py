from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
# import jsonfield
# Create your models here.


class User(AbstractUser):
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True, null=True)
    country = models.CharField(max_length=132, null=True)
    bio = models.TextField(null=True)
    # default="avatar.svg") to be uncommented after setting up a default image
    avatar = models.ImageField(null=True)
    JobTitle = models.CharField(max_length=132, null=True)
    position = models.CharField(max_length=132, null=True)
    is_hr = models.BooleanField(default=False, null=True)
    is_team_leader = models.BooleanField(default=False, null=True)

    def str(self):
        return f'{self.username}, {self.email}'
