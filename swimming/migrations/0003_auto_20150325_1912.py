# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('swimming', '0002_auto_20150325_1850'),
    ]

    operations = [
        migrations.RenameField(
            model_name='team',
            old_name='atheletes',
            new_name='athletes',
        ),
    ]
