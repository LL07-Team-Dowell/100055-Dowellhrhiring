from django.contrib import admin

# Register your models here.
from .models import JobApplication, Job, Meeting, Project, FreelancersAndInterns


admin.site.register(Job)
admin.site.register(JobApplication)
admin.site.register(Project)
admin.site.register(FreelancersAndInterns)
admin.site.register(Meeting)
