# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-06-12 06:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_desc'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='verified',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
