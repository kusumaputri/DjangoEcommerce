# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kerajinan', '0022_cart_cartitem_variantion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Variation',
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
        migrations.RemoveField(
            model_name='variantion',
            name='product',
        ),
        migrations.DeleteModel(
            name='Variantion',
        ),
        migrations.AddField(
            model_name='cartitem',
            name='variations',
            field=models.ManyToManyField(to='kerajinan.Variation', null=True, blank=True),
            preserve_default=True,
        ),
    ]
