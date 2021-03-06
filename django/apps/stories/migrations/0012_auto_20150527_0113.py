# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0011_auto_20150527_0050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storyimage',
            name='aspect_ratio',
            field=models.FloatField(verbose_name='aspect ratio', choices=[(0.0, 'auto'), (0.5, '1:2 landscape'), (0.6666666666666666, '2:3 landscape'), (0.75, '3:4 landscape'), (1.0, 'square'), (1.3333333333333333, '4:3 portrait'), (1.5, '3:2 portrait'), (2.0, '2:1 portrait'), (100.0, 'original')], default=0.0, help_text='height / width'),
        ),
        migrations.AlterField(
            model_name='storyvideo',
            name='aspect_ratio',
            field=models.FloatField(verbose_name='aspect ratio', choices=[(0.0, 'auto'), (0.5, '1:2 landscape'), (0.6666666666666666, '2:3 landscape'), (0.75, '3:4 landscape'), (1.0, 'square'), (1.3333333333333333, '4:3 portrait'), (1.5, '3:2 portrait'), (2.0, '2:1 portrait'), (100.0, 'original')], default=0.0, help_text='height / width'),
        ),
    ]
