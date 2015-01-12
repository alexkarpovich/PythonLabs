# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_projectrole'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectParticipation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=265)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
