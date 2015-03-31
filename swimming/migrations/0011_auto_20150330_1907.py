# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('swimming', '0010_auto_20150330_1904'),
    ]

    operations = [
        migrations.RenameField(
            model_name='team',
            old_name='male_head_coach',
            new_name='head_coach',
        ),
        migrations.RemoveField(
            model_name='team',
            name='female_head_coach',
        ),
    ]
