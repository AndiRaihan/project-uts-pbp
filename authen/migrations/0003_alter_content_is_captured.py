# Generated by Django 4.1 on 2022-10-28 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authen', '0002_content_userprofile_alias_contentupvote_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='is_captured',
            field=models.BooleanField(default=False),
        ),
    ]
