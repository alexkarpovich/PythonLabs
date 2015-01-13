# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=255)),
            ],
            options={
                'ordering': ['name'],
                'db_table': 'tags',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TagCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=255)),
            ],
            options={
                'ordering': ['name'],
                'db_table': 'tags_categories',
                'verbose_name_plural': 'categories',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='tag',
            name='category',
            field=models.ForeignKey(to='tags.TagCategory'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='tag',
            unique_together=set([('name', 'category')]),
        ),
    ]
