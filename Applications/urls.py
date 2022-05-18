from django.urls import path

from .views import application_view, get_jobs, add_new_job, get_applications, candindateview
# from .views import UpdateaACStatus,
from .views import hrview, update_job, delete_job, add_application, project

urlpatterns = [
    path('get_jobs/', get_jobs, name='get_jobs'),
    path('add_job/', add_new_job, name='add_new_job'),
    path('update_job/', update_job, name="update_job"),
    path('delete_job/', delete_job, name="delete_job"),

    path('project/', project, name="project"),

    path('get_applications/', get_applications, name="get_applications"),
    path('add_application/', add_application, name="add_application"),

    path('candindateview/', candindateview, name="candindateview"),
    path('application_view/', application_view, name='application_view'),
    path('hrview/', hrview, name="hrview"),

]
