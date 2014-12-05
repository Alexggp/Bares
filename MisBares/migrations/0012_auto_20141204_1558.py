# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MisBares', '0011_auto_20141203_1847'),
    ]

    operations = [
        migrations.CreateModel(
            name='BarImages_d',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'uploads/images/%Y/%m/%d')),
                ('bar', models.ForeignKey(to='MisBares.Bar_db')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='BarImages_db',
        ),
    ]
