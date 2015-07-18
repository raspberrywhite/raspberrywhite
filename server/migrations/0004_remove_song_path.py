# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0003_song_rawfile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='path',
        ),
    ]
