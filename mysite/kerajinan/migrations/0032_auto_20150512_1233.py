# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kerajinan', '0031_cartitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='variation',
            name='product',
        ),
        migrations.RemoveField(
            model_name='cartitem',
            name='variations',
        ),
        migrations.DeleteModel(
            name='Variation',
        ),
    ]
