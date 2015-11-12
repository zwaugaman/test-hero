# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import s3direct.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cat',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('video', s3direct.fields.S3DirectField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Kitten',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('video', s3direct.fields.S3DirectField(blank=True)),
                ('image', s3direct.fields.S3DirectField(blank=True)),
                ('pdf', s3direct.fields.S3DirectField(blank=True)),
                ('mother', models.ForeignKey(to='cat.Cat')),
            ],
        ),
    ]
