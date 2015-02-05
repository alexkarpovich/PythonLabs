# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0004_auto_20150120_2159'),
        ('project', '0007_project_logo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('employee', models.ForeignKey(to='employee.Employee')),
                ('project', models.ForeignKey(to='project.Project')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterModelOptions(
            name='projectstatus',
            options={'ordering': ['name']},
        ),
        migrations.AddField(
            model_name='project',
            name='members',
            field=models.ManyToManyField(to='employee.Employee', through='project.Membership'),
            preserve_default=True,
        ),
    ]
