# Generated by Django 5.0.1 on 2024-05-29 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hospital_app', '0011_appointment_doctor'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='billed',
            field=models.BooleanField(default=False),
        ),
    ]
