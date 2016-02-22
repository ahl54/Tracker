# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-15 16:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0007_alter_validators_add_error_messages'),
        ('tracker', '0015_auto_20160215_1435'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trackergroup',
            name='permissions',
        ),
        migrations.AddField(
            model_name='tracker',
            name='name',
            field=models.CharField(default=None, max_length=3000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='trackeruser',
            name='group',
            field=models.ManyToManyField(to='auth.Group'),
        ),
        migrations.AlterField(
            model_name='trackergroup',
            name='access_link',
            field=models.URLField(blank=True, max_length=3000),
        ),
        migrations.AlterField(
            model_name='trackergroup',
            name='description',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
