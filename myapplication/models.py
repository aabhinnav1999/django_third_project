from django.db import models

# Create your models here.
class student(models.Model):
    first_name=models.CharField(max_length=25)
    last_name=models.CharField(max_length=25)
    dept=models.CharField(max_length=25)
    age=models.IntegerField()