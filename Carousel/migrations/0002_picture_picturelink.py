# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Carousel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='picture',
            name='PictureLink',
            field=models.URLField(max_length=500, default='www.tubmlr.com'),
            preserve_default=False,
        ),
    ]
