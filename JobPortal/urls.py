
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/v1/auth/", include("djoser.urls")),
    path("api/v1/auth/", include("djoser.urls.jwt")),
    path('api/tasks/', include('Tasks.urls')),
    path('api/jobs/', include('Applications.urls')),
]
