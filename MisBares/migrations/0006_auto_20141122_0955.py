# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MisBares', '0005_auto_20141120_1532'),
    ]

    operations = [
        migrations.AddField(
            model_name='bar_db',
            name='litre',
            field=models.DecimalField(default=0, max_digits=4, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bar_db',
            name='tapa',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
