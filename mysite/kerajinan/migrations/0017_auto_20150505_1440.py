# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kerajinan', '0016_auto_20150430_0929'),
    ]

    operations = [
        migrations.RenameField(
            model_name='static',
            old_name='images1',
            new_name='images',
        ),
    ]
