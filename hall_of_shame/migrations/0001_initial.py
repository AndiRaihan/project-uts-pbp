# Generated by Django 4.1 on 2022-11-01 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Corruptor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('arrested_date', models.DateField()),
                ('corruption_type', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('created_date', models.DateField(auto_now=True)),
            ],
        ),
    ]
