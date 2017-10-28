# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-28 14:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('share', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='collaborators',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='share.CustomUser'),
            preserve_default=False,
        ),
    ]
