# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-08-21 00:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_auto_20190820_1228'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='article_image',
            field=models.ImageField(default=None, upload_to='articles/'),
        ),
    ]
