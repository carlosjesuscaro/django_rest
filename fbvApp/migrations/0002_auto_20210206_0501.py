# Generated by Django 3.1.6 on 2021-02-06 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fbvApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='score',
            field=models.DecimalField(decimal_places=3, max_digits=10),
        ),
    ]