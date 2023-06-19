# Generated by Django 4.2.2 on 2023-06-19 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_account_avatar_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='avatar_img',
        ),
        migrations.AddField(
            model_name='account',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/avatar/'),
        ),
    ]
