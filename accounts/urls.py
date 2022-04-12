from django.urls import path
from .Api import AddUser , UpdateStatus, MyTokenObtainPairView
#from .views import login_view, candidate_view

urlpatterns = [
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/addUser', AddUser.as_view(), name = 'User Sign Up'),
    path('api/updateStatus', UpdateStatus.as_view() , name = 'Update Status'),
    #path('login/',  login_view, name = 'login-view'),
    #path('candidate-view/',  candidate_view, name = 'candidate-view'),
]