# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-28 19:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('share', '0004_auto_20171028_1555'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='pub_date',
            new_name='publish_date',
        ),
    ]