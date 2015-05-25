# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('kerajinan', '0037_auto_20150512_1238'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='update_date',
        ),
        migrations.AddField(
            model_name='product',
            name='updated',
            field=models.DateTimeField(default=datetime.date(2015, 5, 13), auto_now=True),
            preserve_default=False,
        ),
    ]
