# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-09 19:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0009_merge'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tracker',
            old_name='key',
            new_name='uuid',
        ),
        migrations.AddField(
            model_name='tracker',
            name='L1',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tracker',
            name='confirmation',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tracker',
            name='group',
            field=models.CharField(choices=[(b'0', b'Private'), (b'1', b'CBTTC'), (b'2', b'SU2C'), (b'9', b'PUBLIC')], default=b'0', max_length=3000),
        ),
        migrations.AddField(
            model_name='tracker',
            name='subscription',
            field=models.CharField(choices=[(b'0', b'Unsubscribe'), (b'1', b'Available'), (b'2', b'Step')], default=b'0', max_length=20),
        ),
        migrations.AddField(
            model_name='tracker',
            name='summary',
            field=models.CharField(choices=[(b'0', b'None'), (b'1', b'Weekly'), (b'2', b'Monthly')], default=b'0', max_length=7),
        ),
        migrations.AlterField(
            model_name='tracker',
            name='trackerID',
            field=models.CharField(choices=[(b'0', b'Requested'), (b'1', b'Downloaded'), (b'2', b'Staged'), (b'3', b'Database'), (b'4', b'CbioPortal'), (b'5', b'Cavatica')], default=b'0', max_length=11),
        ),
    ]
