# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('swimming', '0004_auto_20150328_2027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='athletes',
            field=models.ManyToManyField(to=b'swimming.Athlete', null=True, blank=True),
        ),
    ]
