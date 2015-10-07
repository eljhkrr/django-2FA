# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myauth', '0003_auto_20151007_0209'),
    ]

    operations = [
        migrations.AddField(
            model_name='two_factor',
            name='phone_verified',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
