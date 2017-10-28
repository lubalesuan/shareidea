# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-28 14:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('share', '0002_auto_20171028_1011'),
    ]

    operations = [
        migrations.AddField(
            model_name='categories',
            name='project_list',
            field=models.ManyToManyField(to='share.Project'),
        ),
        migrations.RemoveField(
            model_name='project',
            name='collaborators',
        ),
        migrations.AddField(
            model_name='project',
            name='collaborators',
            field=models.ManyToManyField(to='share.CustomUser'),
        ),
    ]
