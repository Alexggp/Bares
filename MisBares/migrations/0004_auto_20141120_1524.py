# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MisBares', '0003_bar'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bar_db',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('street', models.CharField(max_length=30)),
                ('price', models.DecimalField(max_digits=4, decimal_places=2)),
                ('latitude', models.DecimalField(max_digits=15, decimal_places=13)),
                ('longitude', models.DecimalField(max_digits=15, decimal_places=13)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='Bar',
        ),
    ]
