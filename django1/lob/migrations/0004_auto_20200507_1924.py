# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-05-07 10:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lob', '0003_person'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('board_id', models.IntegerField()),
                ('title', models.CharField(max_length=200)),
                ('contents', models.TextField()),
                ('writer', models.CharField(max_length=200)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Person',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
