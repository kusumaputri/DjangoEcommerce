# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('kerajinan', '0018_product_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='update_date',
            field=models.DateTimeField(default=datetime.date(2015, 5, 8)),
            preserve_default=False,
        ),
    ]
