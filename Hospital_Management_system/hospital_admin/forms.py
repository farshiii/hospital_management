from django import forms
from .models import Doctor, Department


class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['doctor_name', 'department', 'qualification', 'from_day', 'to_day', 'timing_from', 'timing_to', 'image']

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['name', 'image']
