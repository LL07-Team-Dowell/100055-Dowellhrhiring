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
        return f'{self.project_name}-{self.project_leader}'


class Job(models.Model):
    title = models.CharField(max_length=100, null=False)
    description = models.TextField(null=False)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    CHOICES = (
        ('Not Receiving Applications', 'Not Receiving Applications'),
        ('Receiving Applications', 'Receiving Applications'),
    )
    status = models.CharField(
        max_length=100, choices=CHOICES, default="Not Receiving Applications")
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
    hr_remarks = models.CharField(max_length=500, null=True)
    status = models.CharField(max_length=132, null=True, default="Pending")
    others = models.JSONField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Job Applications'

    def __str__(self):
        return f'{self.job}-{self.applicant}'


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

    def __str__(self):
        return f'{self.applicant}-{self.interviewer}'


class FreelancersAndInterns(models.Model):

    freelancer = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="interns_and_freelancers")
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    hr_remarks = models.CharField(max_length=500, null=True)
    tl_remarks = models.CharField(max_length=500, null=True)
    CHOICES = (
        ('Rehire', 'Rehire'),
        ('Reject', 'Reject'),
    )
    status = models.CharField(max_length=70, choices=CHOICES, default="Rehire")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.freelancer.username}-{self.project}'

    class Meta:
        verbose_name_plural = 'Freelancers And Interns'


class RehiredCandidates(models.Model):
    freelancer = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="rehired_freelancers")
    job_applied = models.ForeignKey(Job, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    tl_remarks = models.CharField(max_length=500, null=True)
    CHOICES = (
        ('Rehire', 'Rehire'),
        ('Reject', 'Reject'),
        ('Pay', 'Pay'),
    )
    teamlead_options = models.CharField(
        max_length=70, choices=CHOICES, default="Rehire")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.freelancer.username}-{self.project}'

    class Meta:
        verbose_name_plural = 'Rehired Freelancers'
