# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MisBares', '0008_auto_20141202_1532'),
    ]

    operations = [
        migrations.CreateModel(
            name='Files_db',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('file', models.FileField(upload_to=b'')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
