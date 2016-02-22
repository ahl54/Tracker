# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0003_auto_20151112_1542'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tracker',
            old_name='access',
            new_name='openAccess',
        ),
        migrations.RemoveField(
            model_name='tracker',
            name='link',
        ),
        migrations.AlterField(
            model_name='tracker',
            name='priority',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
