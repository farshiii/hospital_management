# Generated by Django 5.0.1 on 2024-06-04 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hospital_app', '0016_appointment_email_appointment_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone', models.PositiveIntegerField(default=0)),
                ('email', models.EmailField(default='', max_length=100)),
                ('message', models.CharField(max_length=200)),
            ],
        ),
    ]
