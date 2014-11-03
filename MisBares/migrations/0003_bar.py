# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MisBares', '0002_auto_20141103_1022'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bar',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('price', models.DecimalField(max_digits=4, decimal_places=2)),
                ('latitude', models.DecimalField(max_digits=9, decimal_places=7)),
                ('longitude', models.DecimalField(max_digits=9, decimal_places=7)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
