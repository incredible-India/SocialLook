# Generated by Django 4.1.1 on 2022-09-08 10:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_users_account_post'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='post',
            new_name='posts',
        ),
        migrations.AlterField(
            model_name='users',
            name='account',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 9, 8, 16, 20, 14, 487960), null=True),
        ),
    ]