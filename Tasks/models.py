from django.db import models
from accounts.models import User

STATUS_CHOICES = (
    ('Complete', 'Complete'),
    ('Incomplete', 'Incomplete'),
)


class Task(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='created_user')
    updated_by=models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='updated_user')
    task = models.CharField(max_length=132, null=True)
    status = models.CharField(
        max_length=24, choices=STATUS_CHOICES, default='Incomplete', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.task
