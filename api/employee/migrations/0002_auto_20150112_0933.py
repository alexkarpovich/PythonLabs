# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=45)),
            ],
            options={
                'db_table': 'education',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EmployeeEducation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('education', models.ForeignKey(to='employee.Education')),
                ('employee', models.ForeignKey(to='employee.Employee')),
            ],
            options={
                'db_table': 'employee_education',
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='employeeeducation',
            unique_together=set([('employee', 'education')]),
        ),
        migrations.AlterField(
            model_name='employee',
            name='phone',
            field=models.CharField(default=None, max_length=64, blank=True),
            preserve_default=True,
        ),
    ]
