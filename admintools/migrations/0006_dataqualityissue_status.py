# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-10 08:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admintools', '0005_auto_20170724_2246'),
    ]

    operations = [
        migrations.AddField(
            model_name='dataqualityissue',
            name='status',
            field=models.CharField(choices=[('active', 'Active'), ('ignored', 'Ignored')], default='active', max_length=10),
        ),
    ]
