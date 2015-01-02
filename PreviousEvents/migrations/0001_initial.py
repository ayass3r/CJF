# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EventPicture',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('EventPictureTitle', models.CharField(max_length=100)),
                ('EventPictureUpload', models.ImageField(upload_to='EventPictureImages')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SoundCloud',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('SoundTitle', models.CharField(max_length=100)),
                ('SoundLink', models.URLField(max_length=300)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Youtube',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('VideoTitle', models.CharField(max_length=100)),
                ('VideoLink', models.URLField(max_length=300)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
