# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-03 18:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0007_auto_20160202_1440'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tracker',
            name='L1',
        ),
        migrations.AlterField(
            model_name='tracker',
            name='trackerID',
            field=models.CharField(choices=[(b'Requested', b'Requested'), (b'Downloaded', b'Downloaded'), (b'Staged', b'Staged'), (b'Database', b'Database'), (b'CbioPortal', b'CbioPortal'), (b'Cavatica', b'Cavatica')], default=b'Requested', max_length=11),
        ),
    ]
