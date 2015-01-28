# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0003_auto_20150119_1447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeetag',
            name='employee',
            field=models.ForeignKey(related_name='employee', to='employee.Employee'),
            preserve_default=True,
        ),
    ]
