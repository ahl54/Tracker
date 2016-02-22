# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0002_auto_20151203_1046'),
    ]

    operations = [
        migrations.AddField(
            model_name='tracker',
            name='requester_name',
            field=models.CharField(default='null', max_length=3000),
            preserve_default=False,
        ),
    ]
