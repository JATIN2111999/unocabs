# Generated by Django 3.2.8 on 2021-11-18 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0008_ride_applied'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ride',
            name='applied',
            field=models.TextField(blank=True),
        ),
    ]
