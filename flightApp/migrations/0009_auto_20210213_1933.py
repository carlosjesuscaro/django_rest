# Generated by Django 3.1.6 on 2021-02-13 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flightApp', '0008_auto_20210213_1925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='flightNumber',
            field=models.CharField(max_length=10),
        ),
    ]
