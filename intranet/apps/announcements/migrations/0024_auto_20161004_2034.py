# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-05 00:34
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import intranet.utils.deletion


class Migration(migrations.Migration):

    dependencies = [('announcements', '0023_auto_20160828_2058')]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=intranet.utils.deletion.set_historical_user, to=settings.AUTH_USER_MODEL),),
        migrations.AlterField(
            model_name='announcementrequest',
            name='posted_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=intranet.utils.deletion.set_historical_user, related_name='posted_by',
                                    to=settings.AUTH_USER_MODEL),),
        migrations.AlterField(
            model_name='announcementrequest',
            name='rejected_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=intranet.utils.deletion.set_historical_user, related_name='rejected_by',
                                    to=settings.AUTH_USER_MODEL),),
        migrations.AlterField(
            model_name='announcementrequest',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=intranet.utils.deletion.set_historical_user, related_name='user',
                                    to=settings.AUTH_USER_MODEL),),
    ]
