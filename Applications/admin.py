from django.contrib import admin

# Register your models here.
from .models import JobApplication, Job, Meeting, Product, FreelancersAndInterns, Team, Alert
from .models import Task

admin.site.register(Job)
admin.site.register(JobApplication)
admin.site.register(Product)
admin.site.register(FreelancersAndInterns)
admin.site.register(Meeting)
admin.site.register(Team)
admin.site.register(Alert)
admin.site.register(Task)
