from django.db import models
from accounts.models import User
# Create your models here.


class Project(models.Model):
    project_name = models.CharField(max_length=100)
    project_leader = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.project_name, self.project_leader


class Job(models.Model):
    title = models.CharField(max_length=100, null=False)
    description = models.TextField(null=False)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=100, default="Not Receiving Applications")
    general_terms = models.JSONField(null=True)
    qualification = models.CharField(max_length=132, null=True)
    Technical_Specifications = models.JSONField()
    Payment_terms = models.JSONField()
    others = models.JSONField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class JobApplication(models.Model):
    applicant = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    job = models.ForeignKey(Job, on_delete=models.CASCADE, null=True)
    feedBack = models.TextField(null=True)
    freelancePlatform = models.CharField(max_length=132, null=True)
    freelancePlatformUrl = models.URLField(null=True)
    country = models.CharField(max_length=132, null=True)
    remarks_hr = models.CharField(max_length=500, null=True)
    remarks_tl = models.CharField(max_length=500, null=True)
    status = models.CharField(max_length=132, null=True, default="Pending")
    others = models.JSONField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Job Applications'

    def str(self):
        return f'{self.job}, {self.applicant}'


class Meeting(models.Model):
    date_applied = models.DateTimeField()
    applicant = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="applicants")
    interviewer = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="interviewers")
    job_applied = models.ForeignKey(Job, on_delete=models.CASCADE)
    remarks = models.CharField(max_length=200)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, default="Pending")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
