# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-31 03:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='squawk',
            name='question_text',
        ),
        migrations.AddField(
            model_name='squawk',
            name='squawk_text',
            field=models.CharField(default='Default', max_length=141),
            preserve_default=False,
        ),
    ]