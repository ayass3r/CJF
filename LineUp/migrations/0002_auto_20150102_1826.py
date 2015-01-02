# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LineUp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('ArtistName', models.CharField(max_length=30)),
                ('ArtistInfo', models.CharField(max_length=500)),
                ('PlaceOfOrigin', models.CharField(max_length=100)),
                ('YearsRunning', models.CharField(max_length=20)),
                ('ArtistsImage', models.ImageField(upload_to='LineupImages')),
                ('ArtistTwitter', models.URLField(max_length=300)),
                ('ArtistFacebook', models.URLField(max_length=300)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='Artists',
        ),
    ]
