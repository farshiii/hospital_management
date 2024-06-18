from django.db import models
from Hospital_app.models import Appointment


class Invoice(models.Model):
    PAYMENT_METHOD_CHOICES = [
        ('Cash', 'Cash'),
        ('Card', 'Card'),
        ('UPI', 'UPI'),
    ]

    appointment = models.OneToOneField(Appointment, on_delete=models.CASCADE)
    patient = models.CharField(max_length=255, default=False)
    doctor = models.CharField(max_length=255, default=False)
    appointment_charge_rate = models.DecimalField(max_digits=10, decimal_places=2, default=100.00)
    appointment_quantity = models.PositiveIntegerField(default=1)
    appointment_total = models.PositiveIntegerField(default=0)
    service_charge_rate = models.DecimalField(max_digits=10, decimal_places=2, default=50.00)
    service_quantity = models.PositiveIntegerField(default=0)
    service_total = models.PositiveIntegerField(default=0)
    date = models.DateField(auto_now_add=True)
    payment_mode = models.CharField(max_length=10, choices=PAYMENT_METHOD_CHOICES)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Invoice {self.id} - {self.patient} - {self.date}"

    def calculate_total(self):
        return (self.appointment_charge_rate * self.appointment_quantity) + (
                    self.service_charge_rate * self.service_quantity)

    def calculate_appointment_total(self):
        return self.appointment_charge_rate * self.appointment_quantity

    def calculate_service_total(self):
        return self.service_charge_rate * self.service_quantity

    def save(self, *args, **kwargs):
        self.total_amount = self.calculate_total()
        self.appointment_total = self.calculate_appointment_total()
        self.service_total = self.calculate_service_total()
        super().save(*args, **kwargs)


