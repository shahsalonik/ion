# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-05 01:35
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import intranet.utils.deletion


class Migration(migrations.Migration):

    dependencies = [('eighth', '0044_auto_20161004_2034')]

    operations = [
        migrations.AlterField(
            model_name='eighthsponsor',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=intranet.utils.deletion.handle_eighth_sponsor_deletion,
                                       to=settings.AUTH_USER_MODEL),),
    ]
