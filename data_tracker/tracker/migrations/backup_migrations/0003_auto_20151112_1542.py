# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0002_auto_20151112_1514'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tracker',
            name='name',
            field=models.CharField(max_length=3000),
        ),
    ]
