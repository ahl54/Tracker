# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0004_delete_tracker'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tracker',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('requester_name', models.CharField(max_length=3000)),
                ('email', models.EmailField(max_length=254)),
                ('accession', models.CharField(max_length=200)),
                ('study_name', models.CharField(max_length=3000)),
                ('source', models.CharField(max_length=3000)),
                ('link', models.URLField(max_length=3000)),
                ('samples', models.IntegerField()),
                ('tissue', models.CharField(max_length=3000)),
                ('adult_or_pediatric', models.NullBooleanField()),
                ('citation', models.IntegerField()),
                ('details', models.CharField(max_length=3000)),
                ('priority', models.IntegerField(default=0)),
                ('trackerID', models.IntegerField(default=0)),
            ],
            options={
                'managed': True,
            },
        ),
    ]
