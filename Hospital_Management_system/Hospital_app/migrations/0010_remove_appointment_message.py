# Generated by Django 5.0.1 on 2024-05-28 20:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Hospital_app', '0009_remove_appointment_email_remove_appointment_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='message',
        ),
    ]