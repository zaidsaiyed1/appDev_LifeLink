# Generated by Django 5.1.1 on 2025-05-19 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_customuser_is_driver'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='is_Gov_Official',
            field=models.BooleanField(default=False),
        ),
    ]
