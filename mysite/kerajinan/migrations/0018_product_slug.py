# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('kerajinan', '0017_auto_20150505_1440'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(default=datetime.date(2015, 5, 8), unique=True),
            preserve_default=False,
        ),
    ]
