from django.contrib import admin

# Register your models here.
from .models import JobApplication, Job, Meeting, Project, FreelancersAndInterns, Team, Alert


admin.site.register(Job)
admin.site.register(JobApplication)
admin.site.register(Project)
admin.site.register(FreelancersAndInterns)
admin.site.register(Meeting)
admin.site.register(Team)
admin.site.register(Alert)
