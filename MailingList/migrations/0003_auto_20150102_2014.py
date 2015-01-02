# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MailingList', '0002_auto_20141228_2339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='email',
            name='e_mail',
            field=models.EmailField(max_length=254),
        ),
    ]
