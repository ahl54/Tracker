# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-07 19:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0003_auto_20160303_1533'),
    ]

    operations = [
        migrations.AddField(
            model_name='tracker',
            name='sample_type',
            field=models.CharField(blank=True, max_length=245),
        ),
        migrations.AlterField(
            model_name='tracker',
            name='dataset_name',
            field=models.CharField(blank=True, max_length=345),
        ),
    ]
