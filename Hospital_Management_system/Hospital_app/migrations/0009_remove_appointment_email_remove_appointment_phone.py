# Generated by Django 5.0.1 on 2024-05-28 20:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Hospital_app', '0008_alter_appointment_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='email',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='phone',
        ),
    ]
