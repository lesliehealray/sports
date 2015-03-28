# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Athlete',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('position', models.CharField(max_length=20)),
                ('height', models.CharField(unique=True, max_length=20)),
                ('year', models.CharField(max_length=20)),
                ('hometown', models.CharField(unique=True, max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=50)),
                ('head_coach', models.CharField(max_length=50)),
                ('school', models.CharField(max_length=50)),
                ('schedule', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=20)),
                ('atheletes', models.ManyToManyField(to='swimming.Athlete')),
            ],
            options={
                'verbose_name_plural': 'Teams',
            },
            bases=(models.Model,),
        ),
    ]
