# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kerajinan', '0033_auto_20150512_1233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variation',
            name='price',
            field=models.DecimalField(null=True, max_digits=65, decimal_places=2, blank=True),
        ),
    ]
