from django.db import models
from django.contrib.auth.models import User

STATUS_CHOICES = (
        ('Complete', 'Complete'),
        ('Incomplete', 'Incomplete'),
    )


class Task(models.Model):
    # user = models.ForeignKey(User , on_delete = models.CASCADE,null = True)
    user = models.CharField(max_length=24, null = True)
    date =  models.DateField()
    task = models.CharField(max_length  = 132, null = True)
    status = models.CharField(max_length=24, choices=STATUS_CHOICES, default='Incomplete', null = True, blank=True)

    def __str__(self):
        return self.task

