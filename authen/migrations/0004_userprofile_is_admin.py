# Generated by Django 4.1 on 2022-10-28 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authen', '0003_alter_content_is_captured'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
    ]