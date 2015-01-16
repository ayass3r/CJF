# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SpecialArtist',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('ArtistName', models.CharField(max_length=30)),
                ('ArtistInfo', models.CharField(max_length=1000)),
                ('PlaceOfOrigin', models.CharField(max_length=100)),
                ('YearsRunning', models.CharField(max_length=20)),
                ('ArtistsImage', models.ImageField(upload_to='SpecialGuestImages')),
                ('ArtistTwitter', models.URLField(max_length=300)),
                ('ArtistFacebook', models.URLField(max_length=300)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
