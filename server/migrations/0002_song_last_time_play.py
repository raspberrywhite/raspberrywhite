# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='last_time_play',
            field=models.BigIntegerField(default=0),
            preserve_default=True,
        ),
    ]
