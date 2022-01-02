# Generated by Django 3.2.6 on 2021-10-15 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0036_auto_20210530_0010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='receive_eighth_emails',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='receive_news_emails',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(
                max_length=35, choices=[("male", "Male"), ("female", "Female"), ("non-binary", "Non-binary")], null=True, blank=True),
        ),
    ]
