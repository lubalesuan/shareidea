# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-02 03:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='projects_wanted',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
    ]
