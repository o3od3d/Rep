# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-05-06 12:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lob', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='data',
        ),
        migrations.AddField(
            model_name='post',
            name='name',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]