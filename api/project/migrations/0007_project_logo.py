# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import easy_thumbnails.fields


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0006_auto_20150121_1413'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='logo',
            field=easy_thumbnails.fields.ThumbnailerImageField(upload_to=b'./project/images/', blank=True),
            preserve_default=True,
        ),
    ]
