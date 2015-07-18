# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import filer.fields.file


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0002_song_last_time_play'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='rawfile',
            field=filer.fields.file.FilerFileField(blank=True, to='filer.File', null=True),
            preserve_default=True,
        ),
    ]
