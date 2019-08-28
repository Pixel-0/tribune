# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-08-27 13:05
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0018_newsletterrecipients'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_image',
            field=models.ImageField(blank=True, upload_to='articles/'),
        ),
        migrations.AlterField(
            model_name='article',
            name='editor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='article',
            name='post',
            field=tinymce.models.HTMLField(),
        ),
        migrations.DeleteModel(
            name='Editor',
        ),
    ]
