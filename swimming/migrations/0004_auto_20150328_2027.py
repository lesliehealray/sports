# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('swimming', '0003_auto_20150325_1912'),
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField()),
                ('location', models.CharField(max_length=100)),
                ('opponent', models.CharField(max_length=100)),
                ('results', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterModelOptions(
            name='team',
            options={'ordering': ('name',)},
        ),
        migrations.RemoveField(
            model_name='team',
            name='schedule',
        ),
        migrations.AlterField(
            model_name='athlete',
            name='height',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='athlete',
            name='hometown',
            field=models.CharField(max_length=100),
        ),
    ]
