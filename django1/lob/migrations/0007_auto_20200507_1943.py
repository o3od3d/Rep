# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-05-07 10:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lob', '0006_auto_20200507_1939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]