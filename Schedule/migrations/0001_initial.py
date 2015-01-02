# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Day',
            fields=[
                ('DayName', models.CharField(unique=True, serialize=False, max_length=20, primary_key=True)),
                ('Price', models.CharField(max_length=8)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Show',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('Artist', models.CharField(max_length=30)),
                ('StartTime', models.DateTimeField()),
                ('EndTime', models.DateTimeField()),
                ('DayName', models.ForeignKey(to='Schedule.Day')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
