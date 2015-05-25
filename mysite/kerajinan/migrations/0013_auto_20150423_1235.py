# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kerajinan', '0012_auto_20150423_1211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to=b'media'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(max_digits=10, decimal_places=2),
        ),
    ]
