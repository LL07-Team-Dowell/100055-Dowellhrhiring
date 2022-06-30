from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


class UserAdmin(BaseUserAdmin):
    ordering = ["email"]
    model = User
    list_display = ["pkid", "id", "email", "username",
                    "first_name", "last_name", "is_staff", "is_active"]
    list_display_links = ["id", "email"]
    list_filter = ["email", "username", "first_name",
                   "last_name", "is_staff", "is_active"]


admin.site.register(User, UserAdmin)
