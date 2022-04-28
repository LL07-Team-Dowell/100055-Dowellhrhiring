from django.urls import path
from .views import get_users, register_user

urlpatterns = [
    path('register_user/', register_user, name='register_user'),
    path('get_users/', get_users, name='get_users'),
    #path('login/', login, name='login'),
]
