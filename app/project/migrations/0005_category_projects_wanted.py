# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-02 03:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0004_project_collaborators'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='projects_wanted',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
    ]
