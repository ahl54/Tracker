# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-16 20:30
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0017_auto_20160215_1615'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tracker',
            options={'ordering': ('-id', 'time', 'priority'), 'permissions': (('private', 'Can be seen and used by the owner only'), ('view_only', 'Can be only viewed by anyone'), ('user_limited', 'Can be seen by select users only'), ('group_limited', 'Can be accessed by a group or multiple groups'), ('public', 'Can be viewed and used by anyone'))},
        ),
        migrations.AddField(
            model_name='trackeruser',
            name='username',
            field=models.CharField(blank=True, max_length=45, null=True),
        ),
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
            name='details',
            field=models.CharField(blank=True, max_length=3000),
        ),
        migrations.AlterField(
            model_name='tracker',
            name='link',
            field=models.URLField(blank=True, max_length=3000),
        ),
        migrations.AlterField(
            model_name='tracker',
            name='name',
            field=models.CharField(default=b'source_cancer_type_number', max_length=3000),
        ),
        migrations.AlterField(
            model_name='tracker',
            name='priority',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='tracker',
            name='requester_name',
            field=models.CharField(max_length=3000),
        ),
        migrations.AlterField(
            model_name='tracker',
            name='sample_type',
            field=models.CharField(blank=True, max_length=3000),
        ),
        migrations.AlterField(
            model_name='tracker',
            name='source',
            field=models.CharField(blank=True, max_length=3000),
        ),
        migrations.AlterField(
            model_name='tracker',
            name='study_name',
            field=models.CharField(max_length=3000),
        ),
        migrations.AlterField(
            model_name='tracker',
            name='tissue',
            field=models.CharField(blank=True, max_length=3000),
        ),
        migrations.AlterField(
            model_name='trackeruser',
            name='email',
            field=models.EmailField(db_index=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='trackeruser',
            name='name',
            field=models.CharField(max_length=45),
        ),
        migrations.AlterField(
            model_name='trackeruser',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_id', to=settings.AUTH_USER_MODEL),
        ),
    ]
