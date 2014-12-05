# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import MisBares.models


class Migration(migrations.Migration):

    dependencies = [
        ('MisBares', '0015_auto_20141204_1836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='barimages_db',
            name='image',
            field=models.ImageField(upload_to=MisBares.models.PathAndRename(b'/uploads/images/')),
            preserve_default=True,
        ),
    ]
