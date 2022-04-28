from django.contrib import admin
from .models import Task


class TaskAdmin(admin.ModelAdmin):
    
    list_display = ['id', 'updated_by', 'created_by','task', 'status', 'created', 'updated']
    search_fields = ['user__username']
    
    class Meta:
        model = Task

admin.site.register(Task, TaskAdmin)