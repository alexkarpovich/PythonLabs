# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tag', '0002_auto_20150113_1112'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tagtype',
            options={'ordering': ['name']},
        ),
    ]
