# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('swimming', '0007_auto_20150329_1830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='athlete',
            name='height',
            field=models.CharField(max_length=20, null=True, blank=True),
        ),
    ]
