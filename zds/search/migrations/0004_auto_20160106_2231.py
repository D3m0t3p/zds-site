# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-06 22:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0003_auto_20150820_1950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='searchindexcontent',
            name='tags',
            field=models.ManyToManyField(blank=True, db_index=True, to='search.SearchIndexTag', verbose_name=b'Tags'),
        ),
    ]