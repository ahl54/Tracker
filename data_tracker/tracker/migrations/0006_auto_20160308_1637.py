# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-08 16:37
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0005_document'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='id',
        ),
        migrations.AddField(
            model_name='document',
            name='idtracker_document',
            field=models.IntegerField(default=datetime.datetime(2016, 3, 8, 16, 37, 6, 254868), primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
