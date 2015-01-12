from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class TagCategory(models.Model):
    name = models.CharField(max_length=255, blank=False, default='')

    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        db_table = 'tags_categories'
        ordering = ['name']
        verbose_name_plural = 'categories'


class Tag(models.Model):
    name = models.CharField(max_length=255, blank=False, default='')
    category = models.ForeignKey(TagCategory)

    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        db_table = 'tags'
        ordering = ['name']
        unique_together = ('name', 'category',)


class TaggedItem(models.Model):
    tag = models.ForeignKey(Tag)
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return '{} - {}'.format(self.tag.name, self.tag.category.name)