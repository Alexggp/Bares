# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MisBares', '0018_comments_db'),
    ]

    operations = [
        migrations.AddField(
            model_name='bar_db',
            name='description',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bar_db',
            name='name',
            field=models.CharField(max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bar_db',
            name='street',
            field=models.CharField(max_length=100),
            preserve_default=True,
        ),
    ]
