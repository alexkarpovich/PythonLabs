# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import easy_thumbnails.fields


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0003_auto_20150119_1447'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='photo',
            field=easy_thumbnails.fields.ThumbnailerImageField(upload_to=b'./employee/images/', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='employeetag',
            name='employee',
            field=models.ForeignKey(related_name='employee', to='employee.Employee'),
            preserve_default=True,
        ),
    ]
