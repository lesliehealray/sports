# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('swimming', '0009_auto_20150330_1838'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='head_coach',
        ),
        migrations.AddField(
            model_name='team',
            name='female_head_coach',
            field=models.CharField(max_length=50, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='team',
            name='male_head_coach',
            field=models.CharField(max_length=50, null=True, blank=True),
            preserve_default=True,
        ),
    ]
