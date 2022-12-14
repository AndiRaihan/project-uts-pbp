# Generated by Django 4.1 on 2022-10-29 04:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authen', '0003_alter_content_is_captured'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateField(auto_now_add=True)),
                ('comment', models.TextField()),
                ('commented_on', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authen.content')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authen.userprofile')),
            ],
        ),
    ]
