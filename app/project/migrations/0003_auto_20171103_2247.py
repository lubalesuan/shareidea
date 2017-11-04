# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-03 22:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_auto_20171103_0107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='accept_applicants',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='pitch',
            field=models.TextField(blank=True, max_length=250),
        ),
    ]