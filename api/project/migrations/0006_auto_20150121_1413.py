# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tag', '0003_auto_20150119_1023'),
        ('project', '0005_projectposition'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectTag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('project', models.ForeignKey(to='project.Project')),
                ('tag', models.ForeignKey(to='tag.Tag')),
            ],
            options={
                'db_table': 'project_tag',
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='projecttag',
            unique_together=set([('project', 'tag')]),
        ),
    ]
