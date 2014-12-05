# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MisBares', '0012_auto_20141204_1558'),
    ]

    operations = [
        migrations.CreateModel(
            name='BarImages_db',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'uploads/images/%Y/%m/%d')),
                ('bar', models.ForeignKey(to='MisBares.Bar_db')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='barimages_d',
            name='bar',
        ),
        migrations.DeleteModel(
            name='BarImages_d',
        ),
    ]
