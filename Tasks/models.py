from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

STATUS_CHOICES = (
    ('Complete', 'Complete'),
    ('Incomplete', 'Incomplete'),
)


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    task = models.CharField(max_length=132, null=True)
    decscription = models.CharField(max_length=132, null=True)
    status = models.CharField(
        max_length=24, choices=STATUS_CHOICES, default='Incomplete', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.decscription
