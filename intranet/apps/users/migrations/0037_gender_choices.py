# Generated by Django 3.1.11 on 2021-05-30 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0036_auto_20210530_0010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(
                max_length=35, choices=[("male", "Male"), ("female", "Female"), ("non-binary", "Non-binary")], null=True, blank=True),
        ),
    ]
