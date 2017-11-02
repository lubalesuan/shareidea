# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-02 02:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=20)),
                ('pitch', models.TextField(max_length=250)),
                ('description', models.TextField()),
                ('publish_date', models.DateTimeField(verbose_name='published date')),
                ('accept_applicants', models.BooleanField()),
                ('contact_email', models.EmailField(max_length=254)),
                ('category', models.ManyToManyField(to='project.Category')),
            ],
        ),
    ]
