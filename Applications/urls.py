from django.urls import path

from .views import application_view, get_jobs, add_new_job, get_applications, candidateview
# from .views import UpdateaACStatus,
from .views import hrview, update_job, delete_job, add_application, project, meeting, teams
from .views import Jobs_list_Search, Jobs_application_list_Search, get_my_applications, account_view
from .views import team_lead_view, update_application, delete_application  # get_user

urlpatterns = [
    # jobs
    path('get_jobs/', get_jobs, name='get_jobs'),
    path('add_job/', add_new_job, name='add_new_job'),
    path('update_job/<int:pk>/', update_job, name="update_job"),
    path('delete_job/<int:pk>/', delete_job, name="delete_job"),

    path('project/', project, name="project"),
    path('meeting/', meeting, name="meeting"),
    path('teams/', teams, name="teams"),
    # applications
    path('get_applications/', get_applications, name="get_applications"),
    path('add_application/', add_application, name="add_application"),
    path('update_application/<int:pk>/',
         update_application, name="update_application"),
    path('delete_application/<int:pk>/',
         delete_application, name="delete_application"),
    path('get_my_applications/', get_my_applications, name="get_my_applications"),

    #path('get_user/', get_user, name="get_user"),
    path('candidateview/', candidateview, name="candidateview"),
    path('application_view/', application_view, name='application_view'),
    path('hrview/', hrview, name="hrview"),
    path('account_view/', account_view, name="account_view"),
    path('team_lead_view/', team_lead_view, name="team_lead_view"),
    # search
    path('job_search/', Jobs_list_Search, name='job_search'),
    path('job_applications_search/', Jobs_application_list_Search,
         name='job_applications_search'),
]
