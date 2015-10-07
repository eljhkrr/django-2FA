# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myauth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Two_factor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('phone_number', models.CharField(max_length=20)),
                ('phone_token', models.CharField(max_length=6)),
                ('email_token', models.CharField(max_length=100)),
                ('email_verified', models.BooleanField()),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
