# Generated by Django 5.0.1 on 2024-06-07 15:52

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital_staff', '0008_alter_invoice_payment_mode'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
