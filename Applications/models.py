from django.db import models
from accounts.models import User
# Create your models here.

class Job(models.Model):
    title = models.CharField(max_length=100, null=False)
    description = models.TextField(null=False)
    specific_terms = models.TextField()
    status = models.CharField(
        max_length=100, default="Not Receiving Applications")
    general_terms = models.JSONField(null=True)
    qualification = models.CharField(max_length=132, null=True)
    Technical_Specifications = models.JSONField()
    Payment_terms = models.JSONField()
    others = models.JSONField()

    def __str__(self):
        return self.title


class JobApplication(models.Model):
    applicant = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    job = models.ForeignKey(Job, on_delete=models.CASCADE, null=True)
    feedBack = models.TextField(null=True)
    freelancePlatform = models.CharField(max_length=132, null=True)
    freelancePlatformUrl = models.URLField(null=True)
    country = models.CharField(max_length=132, null=True)
    status = models.CharField(max_length=132, null=True, default="Pending")
    others = models.JSONField()

    class Meta:
        verbose_name_plural = 'Job Applications'

    def str(self):
        return f'{self.job}, {self.applicant}'


class Project(models.Model):
    project_name = models.CharField(max_length=100)
    project_leader = models.ForeignKey(User, on_delete=models.CASCADE)


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
