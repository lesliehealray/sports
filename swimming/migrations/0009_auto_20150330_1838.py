# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('swimming', '0008_auto_20150329_1832'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='gender',
        ),
        migrations.AddField(
            model_name='athlete',
            name='gender',
            field=models.CharField(default='exit', max_length=50),
            preserve_default=False,
        ),
    ]
