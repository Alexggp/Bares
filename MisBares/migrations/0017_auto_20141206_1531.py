# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import MisBares.models


class Migration(migrations.Migration):

    dependencies = [
        ('MisBares', '0016_auto_20141204_1839'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rates_db',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('points', models.IntegerField()),
                ('bar', models.ForeignKey(to='MisBares.Bar_db')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='barimages_db',
            name='image',
            field=models.ImageField(upload_to=MisBares.models.PathAndRename(b'images')),
            preserve_default=True,
        ),
    ]
