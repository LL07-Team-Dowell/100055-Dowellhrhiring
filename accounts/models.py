from django.db import models
from django.contrib.auth.models import User
# import jsonfield
# Create your models here.

class Profile(models.Model):
    image = models.ImageField(null = True) #code to be commented
    id = models.AutoField(primary_key = True)
    JobTitle = models.CharField(max_length = 132,null = True)
    position = models.CharField(max_length = 132,null = True)
    user = models.ForeignKey(User , on_delete = models.CASCADE)

    def __str__(self):
        return str(self.id)


