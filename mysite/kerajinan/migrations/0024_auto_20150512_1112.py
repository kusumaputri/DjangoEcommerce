# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kerajinan', '0023_auto_20150512_1111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='total',
            field=models.DecimalField(default=0.0, max_digits=65, decimal_places=2),
        ),
    ]
