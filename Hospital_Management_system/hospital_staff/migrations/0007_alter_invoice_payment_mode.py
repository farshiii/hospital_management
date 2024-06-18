# Generated by Django 5.0.1 on 2024-05-31 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital_staff', '0006_invoice_appointment_total_invoice_service_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='payment_mode',
            field=models.CharField(choices=[('Cash', 'Cash'), ('Card', 'Card'), ('UPI', 'UPI')], default='Cash', max_length=10),
        ),
    ]