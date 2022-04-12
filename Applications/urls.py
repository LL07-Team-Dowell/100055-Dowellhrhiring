from django.urls import path

from .views import ApplicationView, AddNewJobs , GetJobs, UpdateHRStatus , UpdateTMStatus , UpdateaACStatus, NetworkSpeedView

urlpatterns = [
    path('Apls/' , ApplicationView.as_view() , name = 'Apply for applications Applications'),
    path('Jobs/' , AddNewJobs.as_view() , name = 'get or add Jobs by admin Applications'),
    path('job/', GetJobs.as_view() , name = "get a Users Submitted Jobs"),
    path('updateHrStatus/' , UpdateHRStatus.as_view() , name = "Update status"),
    path('updateTMStatus/' , UpdateTMStatus.as_view() , name = "Update status"),
    path('updateACStatus/' , UpdateaACStatus.as_view() , name = "Update status"),
    path('speed/' , NetworkSpeedView.as_view() , name = 'Network speed'),
]