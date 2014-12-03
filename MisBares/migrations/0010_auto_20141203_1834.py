# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MisBares', '0009_files_db'),
    ]

    operations = [
        migrations.AlterField(
            model_name='files_db',
            name='file',
            field=models.FileField(upload_to=b'/uploads/images'),
            preserve_default=True,
        ),
    ]
