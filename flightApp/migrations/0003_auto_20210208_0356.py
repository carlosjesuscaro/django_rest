# Generated by Django 3.1.6 on 2021-02-08 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flightApp', '0002_passenger_reservation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passenger',
            name='email',
            field=models.CharField(max_length=40),
        ),
    ]