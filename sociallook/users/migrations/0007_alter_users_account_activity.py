# Generated by Django 4.0 on 2022-09-09 08:20

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_rename_post_posts_alter_users_account'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='account',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 9, 9, 13, 50, 47, 499131), null=True),
        ),
        migrations.CreateModel(
            name='activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateofpost', models.DateTimeField(auto_now_add=True)),
                ('whofollow', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='follow', to='users.users')),
                ('whomtofollow', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='follower', to='users.users')),
            ],
        ),
    ]
