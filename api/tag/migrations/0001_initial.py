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
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'tag',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TagCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'tag_category',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TagType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=15)),
            ],
            options={
                'db_table': 'tag_type',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='tagcategory',
            name='tag_type',
            field=models.ForeignKey(to='tag.TagType'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='tag',
            name='tag_category',
            field=models.ForeignKey(to='tag.TagCategory', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='tag',
            name='tag_type',
            field=models.ForeignKey(to='tag.TagType'),
            preserve_default=True,
        ),
    ]
