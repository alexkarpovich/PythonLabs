# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tag', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='tag_category',
            field=models.ForeignKey(blank=True, to='tag.TagCategory', null=True),
            preserve_default=True,
        ),
    ]
