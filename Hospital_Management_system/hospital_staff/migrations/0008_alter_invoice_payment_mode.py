# Generated by Django 5.0.1 on 2024-06-01 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital_staff', '0007_alter_invoice_payment_mode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='payment_mode',
            field=models.CharField(choices=[('Cash', 'Cash'), ('Card', 'Card'), ('UPI', 'UPI')], max_length=10),
        ),
    ]
