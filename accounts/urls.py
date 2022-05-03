from django.urls import path
from .views import get_users, RegisterView, LoginView


urlpatterns = [
    path('register_user/', RegisterView.as_view(), name='register_user'),
    path('get_users/', get_users, name='get_users'),
    path('login_user/', LoginView.as_view(), name='login'),
]
