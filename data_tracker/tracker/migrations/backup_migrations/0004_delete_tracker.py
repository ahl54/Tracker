# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0003_tracker_requester_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Tracker',
        ),
    ]
