
from django.contrib import admin
from django.urls import path, include
<<<<<<< HEAD
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls

=======
>>>>>>> backend

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/accounts/', include('accounts.urls')),
    path('api/tasks/', include('Tasks.urls')),
    path('api/jobs/', include('Applications.urls')),
<<<<<<< HEAD
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('docs/',include_docs_urls(title='JobPortal')),
    path('schema', get_schema_view(
        title="JobPortal",
        description="API for the Hr Hiring ...",
        version="1.0.0",
    ),name="openapi-schema"),
    

=======
>>>>>>> backend
]
