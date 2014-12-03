# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MisBares', '0010_auto_20141203_1834'),
    ]

    operations = [
        migrations.CreateModel(
            name='BarImages_db',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('image', models.ImageField(upload_to=b'uploads/images')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='Files_db',
        ),
    ]
