from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class JobApplication(models.Model):
    id = models.AutoField(primary_key=True)
    feedBack = models.TextField(null=True)
    freelancePlatformUrl = models.URLField(null=True)
    applicationName = models.CharField(max_length=132)
    status = models.CharField(max_length=132, null=True, default="Pending")
    applicationlvl = models.CharField(max_length=132, null=True, default="HR")
    country = models.CharField(max_length=132, null=True)
    username = models.CharField(max_length=132, null=True)
    qualification = models.CharField(max_length=132, null=True)
    freelancePlatform = models.CharField(max_length=132, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    others = models.JSONField()

    def __str__(self):
        return self.applicationName

    class Meta:
        verbose_name_plural = 'JobApplications'


class InternetSpeed(models.Model):

    #  user = models.ForeignKey(User , on_delete = models.CASCADE,null = True)
    user = models.CharField(max_length=24, null=True)
    download_speed = models.CharField(max_length=24, null=True)
    upload_speed = models.CharField(max_length=24, null=True)

    def __str__(self):
        return self.user

    class Meta:
        verbose_name_plural = 'Internet Speeds'


class NewJobsApplication(models.Model):
    feedBack = models.TextField(null=True)
    freelancePlatformUrl = models.URLField(null=True)
    applicationName = models.CharField(max_length=132)
    status = models.CharField(max_length=132, null=True)
    country = models.CharField(max_length=132, null=True)
    username = models.CharField(max_length=132, null=True)
    qualification = models.CharField(max_length=132, null=True)
    freelancePlatform = models.CharField(max_length=132, null=True)
    others = models.JSONField()
    General_Terms_Conditions = models.JSONField()
    Technical_Specifications = models.JSONField()
    Payment_terms = models.JSONField()
    Work_Flow = models.JSONField()

    def __str__(self):
        return self.applicationName

    class Meta:
        verbose_name_plural = 'New JobApplications'


class HRCandidateStatus(models.Model):
    id = models.AutoField(primary_key=True)
    hr_Status = models.CharField(max_length=132, null=True)
    hr_FeedBack = models.CharField(max_length=300, null=True)
    JobApplication = models.ForeignKey(
        JobApplication, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.JobApplication.applicationName

    class Meta:
        verbose_name_plural = 'HR CandidateStatuses'


class TMCandidateStatus(models.Model):
    id = models.AutoField(primary_key=True)
    team_lead_status = models.CharField(max_length=132, null=True)
    team_lead_feedback = models.CharField(max_length=300, null=True)
    JobApplication = models.ForeignKey(
        JobApplication, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name_plural = 'TMCandidateStatuses'


class AccountsCandidateStatus(models.Model):
    id = models.AutoField(primary_key=True)
    accounts_status = models.CharField(max_length=132, null=True)
    accounts_feedback = models.CharField(max_length=132, null=True)
    JobApplication = models.ForeignKey(
        JobApplication, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name_plural = 'AccountsCandidateStatuses'
