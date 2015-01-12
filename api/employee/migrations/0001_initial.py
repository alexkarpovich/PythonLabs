# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=64)),
                ('last_name', models.CharField(max_length=64)),
                ('email', models.CharField(max_length=64)),
                ('summary_description', models.TextField()),
                ('skype', models.CharField(max_length=64)),
                ('phone', models.CharField(max_length=64)),
            ],
            options={
                'db_table': 'employee',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EmployeeLanguage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('level', models.CharField(max_length=2, choices=[(b'b', b'Basic'), (b'pi', b'Pre-intermediate'), (b'i', b'Intermediate'), (b'a', b'Advanced')])),
                ('employee', models.ForeignKey(to='employee.Employee')),
            ],
            options={
                'db_table': 'employee_language',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=45)),
            ],
            options={
                'db_table': 'language',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='employeelanguage',
            name='language',
            field=models.ForeignKey(to='employee.Language'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='employeelanguage',
            unique_together=set([('employee', 'language')]),
        ),
    ]
