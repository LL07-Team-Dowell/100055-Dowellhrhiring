from django.contrib import admin

# Register your models here.
from .models import JobApplication, NewJobsApplication, HRCandidateStatus, TMCandidateStatus, AccountsCandidateStatus

admin.site.register(JobApplication)
admin.site.register(NewJobsApplication)
admin.site.register(HRCandidateStatus)
admin.site.register(AccountsCandidateStatus)
admin.site.register(TMCandidateStatus)
