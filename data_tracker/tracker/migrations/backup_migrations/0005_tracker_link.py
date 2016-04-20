# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0004_auto_20151112_1552'),
    ]

    operations = [
        migrations.AddField(
            model_name='tracker',
            name='link',
            field=models.URLField(max_length=3000, default=uuid.uuid4),
        ),
    ]
