# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-30 02:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0013_auto_20161029_1626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='article_image',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]