from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse


class Department(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="department", blank=False)

    def __str__(self):
        return f"{self.name}"


class Doctor(models.Model):
    doctor_name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, default=False)
    qualification = models.CharField(max_length=100)
    from_day = models.CharField(max_length=20)
    to_day = models.CharField(max_length=20)
    timing_from = models.CharField(max_length=20)
    timing_to = models.CharField(max_length=20)
    image = models.ImageField(upload_to="doctor", blank=False)

    def __str__(self):
        return f"{self.doctor_name}"
