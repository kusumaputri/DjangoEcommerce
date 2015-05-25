# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kerajinan', '0027_auto_20150512_1220'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='cart',
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
        migrations.RemoveField(
            model_name='cartitem',
            name='product',
        ),
        migrations.RemoveField(
            model_name='cartitem',
            name='variations',
        ),
        migrations.DeleteModel(
            name='CartItem',
        ),
        migrations.RemoveField(
            model_name='variation',
            name='product',
        ),
        migrations.DeleteModel(
            name='Variation',
        ),
    ]
