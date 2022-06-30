from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
import uuid
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager
# Create your models here.


class User(AbstractBaseUser, PermissionsMixin):
    pkid = models.BigAutoField(primary_key=True, editable=False, unique=True)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    username = models.CharField(max_length=200, null=False, unique=True)
    first_name = models.CharField(verbose_name=_("First Name"), max_length=255)
    last_name = models.CharField(verbose_name=_("Last Name"), max_length=255)
    email = models.EmailField(unique=True, null=True)
    password = models.CharField(max_length=255)
    country = models.CharField(max_length=132, null=True)
    bio = models.TextField(null=True)
    avatar = models.ImageField(null=True)
    # default="avatar.svg") to be uncommented after setting up a default image
    JobTitle = models.CharField(max_length=132, null=True)
    position = models.CharField(max_length=132, null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_hr = models.BooleanField(default=False, null=True)
    is_team_leader = models.BooleanField(default=False, null=True)
    is_account = models.BooleanField(default=False, null=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "first_name", "last_name"]

    objects = CustomUserManager()

    def str(self):
        return f'{self.username}, {self.email}'
