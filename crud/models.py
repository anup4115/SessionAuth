from django.db import models

# Create your models here.
class Candidate(models.Model):
    name=models.CharField(max_length=30)
    age=models.IntegerField()
    address=models.CharField(max_length=30)
    job=models.CharField(max_length=30)
    salary=models.IntegerField()