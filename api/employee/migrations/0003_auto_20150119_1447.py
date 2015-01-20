# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tag', '0003_auto_20150119_1023'),
        ('employee', '0002_auto_20150112_0933'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeTag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('level', models.CharField(max_length=1, choices=[(b'0', b'Novice'), (b'1', b'Intern'), (b'2', b'Advanced'), (b'3', b'Expert')])),
                ('experience', models.IntegerField()),
                ('last_used', models.DateField()),
                ('employee', models.ForeignKey(to='employee.Employee')),
                ('tag', models.ForeignKey(to='tag.Tag')),
            ],
            options={
                'db_table': 'employee_tag',
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='employeetag',
            unique_together=set([('employee', 'tag')]),
        ),
    ]
