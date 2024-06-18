# Generated by Django 5.0.1 on 2024-05-30 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hospital_app', '0014_appointment_billed'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointment',
            old_name='fullname',
            new_name='first_name',
        ),
        migrations.AddField(
            model_name='appointment',
            name='gender',
            field=models.CharField(choices=[('other', 'Other'), ('male', 'Male'), ('female', 'Female')], default='other', max_length=10),
        ),
        migrations.AddField(
            model_name='appointment',
            name='last_name',
            field=models.CharField(default='', max_length=100),
        ),
    ]
