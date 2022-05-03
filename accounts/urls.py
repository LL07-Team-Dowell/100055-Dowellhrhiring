from django.urls import path
from .views import get_users, RegisterView


urlpatterns = [
    path('register_user/', RegisterView.as_view(), name='register_user'),
    path('get_users/', get_users, name='get_users'),
    #path('login/', login, name='login'),
]
