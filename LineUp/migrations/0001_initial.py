# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artists',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('ArtistName', models.CharField(max_length=30)),
                ('ArtistInfo', models.CharField(max_length=500)),
                ('PlaceOfOrigin', models.CharField(max_length=100)),
                ('YearsRunning', models.CharField(max_length=20)),
                ('ArtistTwitter', models.URLField(max_length=300)),
                ('ArtistFacebook', models.URLField(max_length=300)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
