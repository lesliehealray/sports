# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('swimming', '0005_auto_20150329_1702'),
    ]

    operations = [
        migrations.AddField(
            model_name='athlete',
            name='photo',
            field=models.ImageField(default=1, upload_to=b''),
            preserve_default=False,
        ),
    ]
