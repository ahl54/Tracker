# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-04-13 14:53
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tracker', '0010_auto_20160411_2034'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrackerProject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
            ],
            options={
                'permissions': (('can_write', 'Can write to project'), ('can_read', 'Can read the project'), ('can_execute', 'Can execute on project'), ('can_copy', 'Can copy to project')),
            },
        ),
        migrations.DeleteModel(
            name='Task',
        ),
        migrations.AlterModelOptions(
            name='tracker',
            options={'ordering': ('-id', 'time', 'priority')},
        ),
        migrations.RemoveField(
            model_name='trackergroup',
            name='users',
        ),
        migrations.RemoveField(
            model_name='trackeruser',
            name='is_admin',
        ),
        migrations.AddField(
            model_name='trackergroup',
            name='members',
            field=models.ManyToManyField(through='tracker.TrackerUser', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='trackeruser',
            name='TrackerGroup',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='User', to='tracker.TrackerGroup'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='trackeruser',
            name='User',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='trackerproject',
            name='members',
            field=models.ManyToManyField(through='tracker.TrackerUser', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='trackeruser',
            name='TrackerProject',
            field=models.ForeignKey(default='PUBLIC', on_delete=django.db.models.deletion.CASCADE, to='tracker.TrackerProject'),
            preserve_default=False,
        ),
    ]