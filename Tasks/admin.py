from django.contrib import admin
from .models import Task


class TaskAdmin(admin.ModelAdmin):
    
    list_display = ['__str__', 'user']
    search_fields = ['user__username']
    
    class Meta:
        model = Task

admin.site.register(Task, TaskAdmin)