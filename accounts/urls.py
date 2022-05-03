from django.urls import path
<<<<<<< HEAD
from .views import get_users, register_user

urlpatterns = [
    path('register_user/', register_user, name='register_user'),
    path('get_users/', get_users, name='get_users'),
    #path('login/', login, name='login'),
=======
from .views import get_users, RegisterView, LoginView, UserView


urlpatterns = [
    path('register_user/', RegisterView.as_view(), name='register_user'),
    path('get_users/', get_users, name='get_users'),
    path('login_user/', LoginView.as_view(), name='login'),
    path('user_view/', UserView.as_view(), name='user_view'),
>>>>>>> backend
]
