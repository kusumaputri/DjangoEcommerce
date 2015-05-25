# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('kerajinan', '0015_auto_20150430_0922'),
    ]

    operations = [
        migrations.RenameField(
            model_name='static',
            old_name='images',
            new_name='images1',
        ),
        migrations.AddField(
            model_name='static',
            name='images2',
            field=models.ImageField(default=datetime.date(2015, 4, 30), upload_to=b'slider'),
            preserve_default=False,
        ),
    ]
