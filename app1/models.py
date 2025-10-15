
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Addtask(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    task=models.CharField(max_length=60)
    done=models.BooleanField(default=False)
    deadline=models.DateField(null=True,blank=True)