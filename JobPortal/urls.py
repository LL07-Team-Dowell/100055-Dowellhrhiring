
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , include('accounts.urls')),
    path('api/taks/', include('Tasks.urls')),
    path('api/jobs/', include('Applications.urls')),
]
