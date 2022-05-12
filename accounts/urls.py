from django.urls import path
from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from .views import get_users, RegisterView, LoginView, UserView, LogoutView


urlpatterns = [
    path('register_user/', RegisterView.as_view(), name='register_user'),
    path('get_users/', get_users, name='get_users'),
    path('login_user/', LoginView.as_view(), name='login'),
    path('user_view/', UserView.as_view(), name='user_view'),
    path('logout_user/', LogoutView.as_view(), name='logout_user'),
    # jwt urls
    path('token/', jwt_views.TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
