# Generated by Django 5.0.6 on 2024-05-16 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hospital_app', '0003_appointment_is_completed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='is_completed',
            field=models.BooleanField(default=False),
        ),
    ]
