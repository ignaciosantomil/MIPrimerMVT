# Generated by Django 4.1 on 2022-08-24 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='familiar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('birth', models.DateField()),
                ('dni', models.FloatField(max_length=8)),
            ],
        ),
    ]
