# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-09 18:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0010_merge'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tracker',
            options={},
        ),
        migrations.AddField(
            model_name='tracker',
            name='status',
            field=models.IntegerField(choices=[(0, 'Regular'), (1, 'Manager'), (2, 'Admin')], default=0),
        ),
    ]