# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-21 19:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0004_link_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='votes',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
