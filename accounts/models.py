from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
import uuid
# Create your models here.


class User(AbstractUser, PermissionsMixin):
    pkid = models.BigAutoField(primary_key=True, editable=False, unique=True)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    username = models.CharField(max_length=200, null=False, unique=True)
    email = models.EmailField(unique=True, null=True)
    password = models.CharField(max_length=255)
    country = models.CharField(max_length=132, null=True)
    bio = models.TextField(null=True)
    avatar = models.ImageField(null=True)
    # default="avatar.svg") to be uncommented after setting up a default image
    JobTitle = models.CharField(max_length=132, null=True)
    position = models.CharField(max_length=132, null=True)
    is_hr = models.BooleanField(default=False, null=True)
    is_team_leader = models.BooleanField(default=False, null=True)
    is_account = models.BooleanField(default=False, null=True)

    def str(self):
        return f'{self.username}, {self.email}'
