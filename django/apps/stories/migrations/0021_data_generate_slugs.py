# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-20 21:04
from __future__ import unicode_literals

from django.db import migrations


def forwards(apps, schema_editor):
    models = 'Section', 'StoryType'
    appname = 'stories'
    for modelname in models:
        model = apps.get_model(appname, modelname)
        for instance in model.objects.all():
            # will generate a slug
            instance.save()


def backwards(*args):
    # no action needed
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0020_auto_20161120_2156'),
    ]

    operations = [
        migrations.RunPython(
            code=forwards,
            reverse_code=backwards,
        )
    ]
