# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-10 15:53
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0012_auto_20160209_2013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tracker',
            name='PMID',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tracker',
            name='accession',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='tracker',
            name='citation',
            field=models.CharField(blank=True, max_length=3000),
        ),
        migrations.AlterField(
            model_name='tracker',
            name='confirmation',
            field=models.CharField(choices=[(b'0', b'None'), (b'1', b'Email me a confirmation of my request')], default=b'0', max_length=100),
        ),
        migrations.AlterField(
            model_name='tracker',
            name='details',
            field=models.CharField(blank=True, max_length=3000),
        ),
        migrations.AlterField(
            model_name='tracker',
            name='group',
            field=models.CharField(choices=[(b'0', b'Private'), (b'1', b'CBTTC'), (b'2', b'SU2C'), (b'9', b'PUBLIC')], default=b'0', max_length=3000),
        ),
        migrations.AlterField(
            model_name='tracker',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='tracker',
            name='link',
            field=models.URLField(blank=True, max_length=3000),
        ),
        migrations.AlterField(
            model_name='tracker',
            name='priority',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='tracker',
            name='sample_type',
            field=models.CharField(blank=True, max_length=3000),
        ),
        migrations.AlterField(
            model_name='tracker',
            name='samples',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='tracker',
            name='source',
            field=models.CharField(blank=True, max_length=3000),
        ),
        migrations.AlterField(
            model_name='tracker',
            name='subscription',
            field=models.CharField(choices=[(b'0', b'None'), (b'1', b'Email me when my request is available'), (b'2', b'Email me at every step along the request')], default=b'0', max_length=100),
        ),
        migrations.AlterField(
            model_name='tracker',
            name='summary',
            field=models.CharField(choices=[(b'0', b'None'), (b'1', b'Email me a weekly summary of Data Tracker requests'), (b'2', b'Email me a monthly summary of Data Tracker requests')], default=b'0', max_length=100),
        ),
        migrations.AlterField(
            model_name='tracker',
            name='time',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='tracker',
            name='tissue',
            field=models.CharField(blank=True, max_length=3000),
        ),
        migrations.AlterField(
            model_name='tracker',
            name='trackerID',
            field=models.CharField(choices=[(b'0', b'Requested'), (b'1', b'Downloaded'), (b'2', b'Staged'), (b'3', b'Database'), (b'4', b'CbioPortal'), (b'5', b'Cavatica')], default=b'0', max_length=11),
        ),
    ]
