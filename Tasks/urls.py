<<<<<<< HEAD
# from django.urls import path
from .views import TaskPost
from rest_framework.routers import DefaultRouter

app_name='tasks_api'


router=DefaultRouter()
router.register('', TaskPost, basename='tasks')
urlpatterns=router.urls



# urlpatterns = [
#     path('view_tasks/', tasks_view, name='view_tasks'),
#     path('add_new_task/', add_new_task, name='add_new_task'),
# ]
=======
from django.urls import path
from .views import tasks_view, add_new_task

urlpatterns = [
    path('view_tasks/', tasks_view, name='view_tasks'),
    path('add_new_task/', add_new_task, name='add_new_task'),
]
>>>>>>> backend
