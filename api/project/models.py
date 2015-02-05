from django.db import models
from tag.models import Tag
from easy_thumbnails.fields import ThumbnailerImageField


class Project(models.Model):
    name = models.CharField(max_length=255, blank=False)
    customer = models.CharField(max_length=64, blank=False)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField()
    status = models.ForeignKey('ProjectStatus', blank=False)
    logo = ThumbnailerImageField(upload_to='./project/images/', blank=True)

    def __str__(self):
        return '{}'.format(self.name)


class ProjectStatus(models.Model):
    name = models.CharField(max_length=64, blank=False)

    class Meta():
        ordering = ['name']

    def __str__(self):
        return '{}'.format(self.name)


class ProjectRole(models.Model):
    name = models.CharField(max_length=45, blank=False)

    def __str__(self):
        return '{}'.format(self.name)


class ProjectParticipation(models.Model):
    name = models.CharField(max_length=265, blank=False)

    def __str__(self):
        return '{}'.format(self.name)


class ProjectPosition(models.Model):
    name = models.CharField(max_length=64, blank=False)

    def __str__(self):
        return '{}'.format(self.name)


class ProjectTag(models.Model):
    project = models.ForeignKey(Project)
    tag = models.ForeignKey(Tag)

    class Meta:
        db_table = 'project_tag'
        unique_together = ('project', 'tag',)

    def __str__(self):
        return '{} {}'.format(self.project.name, self.tag.name)
