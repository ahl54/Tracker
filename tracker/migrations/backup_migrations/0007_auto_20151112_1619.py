# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0006_auto_20151112_1615'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tracker',
            name='link',
            field=models.URLField(default=uuid.uuid1, max_length=3000),
        ),
    ]
