# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kerajinan', '0026_auto_20150512_1219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='line_total',
            field=models.DecimalField(default=10.99, max_digits=65, decimal_places=2),
        ),
    ]
