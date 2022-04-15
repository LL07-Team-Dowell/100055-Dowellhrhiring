from django.urls import path
from .Api import AddUser, MyTokenObtainPairView
#from .views import login_view, candidate_view

urlpatterns = [
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/add_user', AddUser.as_view(), name='sign_up'),
    #path('login/',  login_view, name = 'login_view'),
    #path('candidate_view/',  candidate_view, name = 'candidate_view'),
]
