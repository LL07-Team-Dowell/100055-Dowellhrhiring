from django.contrib import admin
from .models import Task


class TaskAdmin(admin.ModelAdmin):
    
<<<<<<< HEAD
    list_display = ['id', 'updated_by', 'created_by','task', 'status', 'created', 'updated']
=======
    list_display = ['__str__', 'user']
>>>>>>> backend
    search_fields = ['user__username']
    
    class Meta:
        model = Task

admin.site.register(Task, TaskAdmin)