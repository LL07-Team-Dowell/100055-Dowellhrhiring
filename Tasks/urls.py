from django.urls import path
from .views import tasks_view, add_new_task

urlpatterns = [
    path('view_tasks/', tasks_view, name='view_tasks'),
    path('add_new_task/', add_new_task, name='add_new_task'),
]
