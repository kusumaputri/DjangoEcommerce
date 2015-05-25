# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kerajinan', '0030_auto_20150512_1225'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantity', models.IntegerField(default=1)),
                ('line_total', models.DecimalField(default=10.99, max_digits=65, decimal_places=2)),
                ('notes', models.TextField(null=True, blank=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('cart', models.ForeignKey(blank=True, to='kerajinan.Cart', null=True)),
                ('product', models.ForeignKey(to='kerajinan.Product')),
                ('variations', models.ManyToManyField(to='kerajinan.Variation', null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
