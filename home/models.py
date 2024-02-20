from django.db import models

# Create your models here



class departments (models.Model):
    dep_name = models.CharField(max_length=10)
    dep_description = models.TextField()
