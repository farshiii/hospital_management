from django import forms
from .models import Appointment, Message


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['first_name', 'last_name', 'email', 'phone', 'department', 'doctor', 'gender']


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['name', 'phone', 'email', 'message']
