# Generated by Django 5.0.1 on 2024-06-07 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hospital_app', '0017_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
