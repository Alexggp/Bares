# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MisBares', '0004_auto_20141120_1524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bar_db',
            name='latitude',
            field=models.DecimalField(max_digits=9, decimal_places=7),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bar_db',
            name='longitude',
            field=models.DecimalField(max_digits=9, decimal_places=7),
            preserve_default=True,
        ),
    ]
