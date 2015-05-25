# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kerajinan', '0004_userprofile_date_of_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to=b'/static/images/upload/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(max_digits=5, decimal_places=2),
        ),
    ]
