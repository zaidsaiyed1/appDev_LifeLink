# Generated by Django 5.1.1 on 2025-04-29 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_remove_ambulancecurrentlocation_prevlat_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ambulancecurrentlocation',
            name='currLat',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='ambulancecurrentlocation',
            name='currLon',
            field=models.FloatField(),
        ),
    ]
