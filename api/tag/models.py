from django.db import models


class TagType(models.Model):
    name = models.CharField(max_length=15)

    class Meta:
        db_table = 'tag_type'
        ordering = ['name']

    def __str__(self):
        return '{}'.format(self.name)


class TagCategory(models.Model):
    name = models.CharField(max_length=255)
    tag_type = models.ForeignKey(TagType)

    class Meta:
        db_table = 'tag_category'

    def __str__(self):
        return '{} {}'.format(self.name, self.tag_type.name)


class Tag(models.Model):
    name = models.CharField(max_length=255)
    tag_type = models.ForeignKey(TagType)
    tag_category = models.ForeignKey(TagCategory, blank=True, null=True)

    class Meta:
        db_table = 'tag'

    def __str__(self):
        return '{}'.format(self.name)
