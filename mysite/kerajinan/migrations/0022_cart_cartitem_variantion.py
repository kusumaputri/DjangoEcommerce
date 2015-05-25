# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kerajinan', '0021_product_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('total', models.DecimalField(default=0.0, max_digits=100, decimal_places=2)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantity', models.IntegerField(default=1)),
                ('line_total', models.DecimalField(default=10.99, max_digits=1000, decimal_places=2)),
                ('notes', models.TextField(null=True, blank=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('cart', models.ForeignKey(blank=True, to='kerajinan.Cart', null=True)),
                ('product', models.ForeignKey(to='kerajinan.Product')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Variantion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category', models.CharField(default=b'size', max_length=120, choices=[(b'size', b'size'), (b'color', b'color'), (b'package', b'package')])),
                ('title', models.CharField(max_length=120)),
                ('price', models.DecimalField(null=True, max_digits=100, decimal_places=2, blank=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('product', models.ForeignKey(to='kerajinan.Product')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
