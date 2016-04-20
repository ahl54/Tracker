# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0008_auto_20151202_1138'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Access',
            new_name='AccessField',
        ),
        migrations.DeleteModel(
            name='PhoneModel',
        ),
        migrations.AddField(
            model_name='tracker',
            name='email',
            field=models.EmailField(default='Unknown', max_length=254),
            preserve_default=False,
        ),
    ]
