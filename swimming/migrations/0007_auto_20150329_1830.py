# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('swimming', '0006_athlete_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='athlete',
            name='height',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
