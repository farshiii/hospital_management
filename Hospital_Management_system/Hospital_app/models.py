from django.contrib.auth.models import User
from django.db import models
from hospital_admin.models import Department
from hospital_admin.models import Doctor


class Appointment(models.Model):
    GENDER = [
        ('other', 'Other'),
        ('male', 'Male'),
        ('female', 'Female'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, default='')
    email = models.EmailField(max_length=100, default='')
    phone = models.IntegerField(max_length=10, default=9404733748)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, default=False)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE,  default=False)
    date = models.DateField(auto_now_add=True)
    gender = models.CharField(max_length=10, choices=GENDER, default='other')
    is_completed = models.BooleanField(default=False)
    is_cancelled = models.BooleanField(default=False)
    status = models.BooleanField(default=True)
    billed = models.BooleanField(default=False)

    def __str__(self):
        return self.first_name + ' - ' + str(self.date)


class Message(models.Model):
    name = models.CharField(max_length=50)
    phone = models.PositiveIntegerField(default=0)
    email = models.EmailField(max_length=100, default='')
    message = models.CharField(max_length=200)

    def __str__(self):
        return self.name
