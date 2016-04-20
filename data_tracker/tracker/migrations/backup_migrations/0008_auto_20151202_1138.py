# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0007_auto_20151112_1619'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhoneModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=12, blank=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
            ],
        ),
        migrations.RenameField(
            model_name='tracker',
            old_name='pediatric',
            new_name='adult_or_pediatric',
        ),
        migrations.RenameField(
            model_name='tracker',
            old_name='name',
            new_name='requester_name',
        ),
        migrations.AddField(
            model_name='tracker',
            name='study_name',
            field=models.CharField(max_length=3000, default='Name'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tracker',
            name='link',
            field=models.URLField(max_length=3000),
        ),
        migrations.AlterField(
            model_name='tracker',
            name='priority',
            field=models.IntegerField(default=0),
        ),
    ]
