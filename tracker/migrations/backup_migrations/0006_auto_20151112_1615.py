# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0005_tracker_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='Access',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('access', models.CharField(max_length=10, choices=[('Open', 'Open'), ('Restricted', 'Restricted'), ('Unknown', 'Unknown')], default='Unknown')),
            ],
        ),
        migrations.RemoveField(
            model_name='tracker',
            name='openAccess',
        ),
    ]
