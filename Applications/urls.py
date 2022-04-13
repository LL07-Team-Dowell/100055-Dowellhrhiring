from django.urls import path

from .views import application_view, add_new_job, get_jobs
# from .views import UpdateaACStatus,
urlpatterns = [
    path('Apis/application_view/', application_view,
         name='application_view'),
    path('Jobs/add_job/', add_new_job,
         name='add_new_job'),
    path('jobs/get_jobs', get_jobs, name="get_jobs"),
    # path('update_status/', Update_status., name="Update_status")
]
