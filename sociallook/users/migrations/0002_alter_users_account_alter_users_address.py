# Generated by Django 4.0 on 2022-09-06 07:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='account',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 9, 6, 13, 7, 19, 51196)),
        ),
        migrations.AlterField(
            model_name='users',
            name='address',
            field=models.TextField(),
        ),
    ]
