# Generated by Django 3.1.6 on 2021-02-13 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flightApp', '0006_auto_20210213_1917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passenger',
            name='firstName',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
