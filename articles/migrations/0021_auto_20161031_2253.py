# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-01 02:53
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0020_auto_20161031_2247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='article_content',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(blank=True), null=True, size=None),
        ),
    ]