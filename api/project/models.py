from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=255)
    customer = models.CharField(max_length=64)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField()
    status = models.ForeignKey('ProjectStatus')

    def __str__(self):
        return self.name


class ProjectStatus(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

class ProjectRole(models.Model):
    name = models.CharField(max_length=45)

    def __str__(self):
        return self.name
