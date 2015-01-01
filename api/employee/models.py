from django.db import models

class Employee(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    summary_description = models.TextField()
    skype = models.CharField(max_length=64)
    phone = models.CharField(max_length=64)
