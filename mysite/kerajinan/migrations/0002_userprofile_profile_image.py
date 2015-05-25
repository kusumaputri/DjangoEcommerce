# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kerajinan', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='profile_image',
            field=models.ImageField(default=b'/static/images/defaultuserimage.jpg', upload_to=b'uploads'),
            preserve_default=True,
        ),
    ]
