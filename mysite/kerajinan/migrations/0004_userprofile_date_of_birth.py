# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('kerajinan', '0003_userprofile_is_staff'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='date_of_birth',
            field=models.DateField(default=datetime.date(2015, 4, 20)),
            preserve_default=False,
        ),
    ]
