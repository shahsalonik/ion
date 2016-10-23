# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-06 15:10
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [migrations.swappable_dependency(settings.AUTH_USER_MODEL)]

    operations = [
        migrations.CreateModel(
            name='CarApplication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('license_plate', models.CharField(max_length=20)),
                ('make', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
                ('year', models.PositiveIntegerField()),
            ],),
        migrations.CreateModel(
            name='ParkingApplication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=50)),
                ('mentorship', models.BooleanField(default=False)),
                ('cars', models.ManyToManyField(to='parking.CarApplication')),
                ('joint_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                                                 related_name='parkingapplication_joint', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parkingapplication',
                                           to=settings.AUTH_USER_MODEL)),
            ],),
    ]
