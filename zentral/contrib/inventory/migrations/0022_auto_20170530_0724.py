# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-30 07:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0021_auto_20170529_1839'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificate',
            name='common_name',
            field=models.TextField(blank=True, null=True),
        ),
    ]