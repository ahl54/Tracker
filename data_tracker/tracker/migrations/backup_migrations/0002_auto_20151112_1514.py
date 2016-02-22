# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tracker',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('accession', models.CharField(max_length=200)),
                ('name', models.DateTimeField(verbose_name='date published')),
                ('source', models.CharField(max_length=3000)),
                ('link', models.SlugField(max_length=3000)),
                ('samples', models.IntegerField()),
                ('tissue', models.CharField(max_length=3000)),
                ('pediatric', models.NullBooleanField()),
                ('citation', models.IntegerField()),
                ('details', models.CharField(max_length=3000)),
                ('access', models.NullBooleanField()),
                ('priority', models.NullBooleanField()),
                ('trackerID', models.IntegerField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='choice',
            name='question',
        ),
        migrations.DeleteModel(
            name='Node',
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]
