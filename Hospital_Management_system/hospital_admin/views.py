import os
from django.conf import settings
from django.http import HttpResponse
from .forms import DoctorForm, DepartmentForm
from .models import Department, Doctor
from django.shortcuts import render
from Hospital_app.models import Appointment, Message
from hospital_staff.models import Invoice
from django.db.models import Count, Sum
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd
import base64


def admin_staff_page(request):
    return render(request, 'admin_panel/admin_staff_page.html')


def admin_home(request):
    # Retrieve counts and sums
    total_appointments = Appointment.objects.count()
    completed_appointments = Appointment.objects.filter(is_completed=True).count()
    total_income = Invoice.objects.aggregate(total_sum=Sum('total_amount'))['total_sum']
    paid_invoices = Appointment.objects.filter(billed=True).count()

    # Data for charts
    appointments_by_status = [
        {'status': 'Completed', 'count': completed_appointments},
        {'status': 'Pending', 'count': total_appointments - completed_appointments}
    ]

    # Retrieve all billed appointments and invoices
    appointments1 = Appointment.objects.filter(billed=True).order_by('date')
    invoices = Invoice.objects.all()

    # Check that the number of appointments matches the number of invoices
    if len(appointments1) != len(invoices):
        # Handle the error if lengths don't match
        return render(request, 'error_template.html',
                      {'error_message': 'Mismatch in the number of appointments and invoices.'})

    # Extract patient names and dates from appointments
    patient_names = [appointment.first_name for appointment in appointments1]
    dates = [appointment.date for appointment in appointments1]

    # Extract total amounts from invoices
    total_amounts = [invoice.total_amount for invoice in invoices]

    # Create a DataFrame with patient names, dates, and total amounts
    data = {
        'patient_name': patient_names,
        'date': dates,
        'total_amount': total_amounts
    }

    df = pd.DataFrame(data)

    # Plotting
    plt.figure(figsize=(10, 6))  # Adjust the figure size as needed
    plt.plot(df['patient_name'], df['total_amount'], marker='o', linestyle='-')
    plt.xlabel('Patient Name')
    plt.ylabel('Total Amount')
    plt.title('Profit on each Appointment')
    plt.xticks(rotation=45)  # Rotate x-axis labels for better readability

    # Save the plot to a file
    plot_filename = 'plot.png'
    plot_path = os.path.join(settings.MEDIA_ROOT, plot_filename)
    plt.savefig(plot_path)

    # Read the saved image file and encode it as base64 data
    with open(plot_path, 'rb') as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode('utf-8')

    message = Message.objects.all()
    # Context for rendering the template
    context = {
        'total_appointments': total_appointments,
        'completed_appointments': completed_appointments,
        'total_income': total_income,
        'paid_invoices': paid_invoices,
        'appointments_by_status': json.dumps(appointments_by_status),
        'data': encoded_image,
        'message': message
    }

    return render(request, 'admin_panel/admin_dash.html', context)



def analytics_view(request):
    total_appointments = Appointment.objects.count()
    completed_appointments = Appointment.objects.filter(is_completed=True).count()
    cancelled_appointments = Appointment.objects.filter(is_cancelled=True).count()
    total_income = Invoice.objects.aggregate(Sum('total_amount'))['total_amount__sum']
    paid_invoices = Appointment.objects.filter(billed=True).count()

    pending_appointments = total_appointments - completed_appointments - cancelled_appointments

    # Data for charts
    appointments_by_status = [
        {'status': 'Completed', 'count': completed_appointments},
        {'status': 'Cancelled', 'count': cancelled_appointments},
        {'status': 'Pending', 'count': pending_appointments}
    ]

    context = {
        'total_appointments': total_appointments,
        'completed_appointments': completed_appointments,
        'total_income': total_income,
        'paid_invoices': paid_invoices,
        'cancelled_appointments': cancelled_appointments,
        'appointments_by_status': json.dumps(appointments_by_status),
    }
    return render(request, 'admin_panel/appointment_dash.html', context)


def adddoctor(request):
    form = DoctorForm()
    if request.POST:
        doctor_name = request.POST['doctor_name']
        department_id = request.POST['category']
        qualification = request.POST['qualification']
        from_day = request.POST['from_day']
        to_day = request.POST['to_day']
        timing_from = request.POST['timing_from']
        timing_to = request.POST['timing_to']
        image = request.FILES['image']

        department = Department.objects.get(pk=department_id)

        doctor = Doctor(doctor_name=doctor_name, department=department, qualification=qualification, from_day=from_day,
                        to_day=to_day, timing_from=timing_from, timing_to=timing_to, image=image)
        doctor.save()
        return HttpResponse('Doctor Form Submitted Successfully!')
    else:
        form = DoctorForm()


    doctor = Doctor.objects.all()
    departments = Department.objects.all()
    return render(request, 'admin_panel/adddoctor.html', {'form': form, 'doctor': doctor, 'departments': departments})


def adddepartment(request):
    form = DepartmentForm()
    if request.POST:
        name = request.POST['name']
        image = request.FILES['image']
        department = Department(name=name, image=image)
        department.save()
        return HttpResponse('Doctor Form Submitted Successfully!')
    else:
        form = DepartmentForm()

    department = Department.objects.all()
    return render(request, 'admin_panel/adddepartment.html', {'department': department, 'form': form})


def doc_details(request):
    return render(request, 'admin_panel/doctor_details.html')


def plot_appointments(request):
    # Retrieve all appointments and invoices
    appointments = Appointment.objects.filter(billed=True).order_by('date')
    invoices = Invoice.objects.all()
    # Check that the number of appointments matches the number of invoices
    if len(appointments) != len(invoices):
        # Handle the error if lengths don't match
        return render(request, 'error_template.html',
                      {'error_message': 'Mismatch in the number of appointments and invoices.'})

    # Extract patient names and dates from appointments
    patient_names = [appointment.first_name for appointment in appointments]
    name = [appointment.first_name for appointment in appointments]
    dates = [appointment.date for appointment in appointments]

    # Extract total amounts from invoices
    total_amounts = [invoice.total_amount for invoice in invoices]

    # Create a DataFrame with patient names, dates, and total amounts
    data = {
        'patient_name': patient_names,
        'date': dates,
        'name': name,
        'total_amount': total_amounts
    }

    df = pd.DataFrame(data)

    # Plotting
    plt.figure(figsize=(10, 6))  # Adjust the figure size as needed
    plt.plot(df['name'], df['total_amount'], marker='o', linestyle='-')
    plt.xlabel('Date')
    plt.ylabel('Total Amount')
    plt.title('Profit on each Appointment')
    plt.xticks(rotation=45)  # Rotate x-axis labels for better readability

    # Save the plot to a file
    plot_filename = 'plot.png'
    plot_path = os.path.join(settings.MEDIA_ROOT, plot_filename)
    plt.savefig(plot_path)

    # Read the saved image file and encode it as base64 data
    with open(plot_path, 'rb') as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode('utf-8')

    total_appointments = Appointment.objects.count()
    completed_appointments = Appointment.objects.filter(is_completed='True').count()
    total_income = Invoice.objects.aggregate(Sum('total_amount'))['total_amount__sum']
    paid_invoices = Appointment.objects.filter(billed=True).count()

    return render(request, 'admin_panel/profit_dash.html',
                  {'data': encoded_image, 'total_appointments': total_appointments,
                   'completed_appointments': completed_appointments, 'total_income': total_income,
                   'paid_invoices': paid_invoices})
