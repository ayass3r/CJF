# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('PictureTitle', models.CharField(max_length=50)),
                ('CarasoulPicture', models.ImageField(upload_to='CarouselImages')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
