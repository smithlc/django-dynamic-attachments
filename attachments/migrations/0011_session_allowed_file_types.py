# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-05 13:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attachments', '0010_property_is_editable'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='allowed_file_types',
            field=models.TextField(blank=True, help_text='Whitespace-separated file types that are allowed for upload.'),
        ),
    ]
