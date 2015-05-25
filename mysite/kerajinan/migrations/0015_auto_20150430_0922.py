# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('kerajinan', '0014_auto_20150423_1416'),
    ]

    operations = [
        migrations.AddField(
            model_name='static',
            name='images',
            field=models.ImageField(default=datetime.date(2015, 4, 30), upload_to=b'slider'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profile_image',
            field=models.ImageField(upload_to=b'profile'),
        ),
    ]
