# Generated by Django 3.2.8 on 2021-11-13 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_ride_list_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='ride',
            name='tel',
            field=models.IntegerField(default=0),
        ),
    ]
