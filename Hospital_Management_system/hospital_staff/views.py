from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from Hospital_app.models import Appointment
from hospital_admin.models import Department, Doctor
from Hospital_app.forms import AppointmentForm
from hospital_staff.models import Invoice



# Create your views here.


def staff_login(request):
    return render(request, 'admin_panel/admin_login.html')


def admin_home(request):
    total = Appointment.objects.all().count()
    appointment = Appointment.objects.filter(is_completed=False)
    billed = Appointment.objects.filter(billed=True, is_completed=True).count()
    pending = Appointment.objects.filter(is_completed=False).count()
    completed = Appointment.objects.filter(is_completed=True).count()
    patientcount = Appointment.objects.filter(status=True).count()
    return render(request, 'staff/home.html', {'patientcount': patientcount, 'appointment': appointment, 'pending': pending, 'completed': completed, 'total': total, 'billed': billed})


def appointment_by_staff(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to a success page or display a success message
            return redirect('admin_appointment')
    else:
        form = AppointmentForm()

    department = Department.objects.all()
    return render(request, 'staff/add_appointment.html', {'form': form, 'department': department})


def completed_appointment(request):
    completed = Appointment.objects.filter(is_completed=True)
    return render(request, 'staff/completed_appointment.html', {'completed': completed})


def pending_appointment(request):
    task = Appointment.objects.filter(is_completed=False)
    return render(request, 'staff/pending_appointment.html', {'task': task})


def appointment_update(request):
    cancelled = Appointment.objects.filter(is_cancelled=True)
    task = Appointment.objects.filter(is_completed=False, is_cancelled=False)
    completed = Appointment.objects.filter(is_completed=True)
    return render(request, 'staff/appointment_todo.html', {'task': task, 'completed': completed, 'cancelled': cancelled })


def mark_as_done(request, task_id):
    task = Appointment.objects.get(id=task_id)
    task.is_completed = True
    task.save()
    return redirect('appointment_update')


def mark_as_cancel(request, task_id):
    task = Appointment.objects.get(id=task_id)
    task.is_cancelled = True
    task.save()
    return redirect('appointment_update')


def mark_as_undone(request, task_id):
    task = Appointment.objects.get(id=task_id)
    task.is_completed = False
    task.save()
    return redirect('appointment_update')


def mark_as_un_cancel(request, task_id):
    task = Appointment.objects.get(id=task_id)
    task.is_cancelled = False
    task.save()
    return redirect('appointment_update')


def delete_task(request, delete_id):
    delete_task = get_object_or_404(Appointment, id=delete_id)
    delete_task.delete()
    return redirect('appointment_update')


def update_task(request, update_id):
    get_task = get_object_or_404(Appointment, id=update_id)
    if request.method == 'POST':
        new_fullname = request.POST.get('new_fullname')
        new_phone = request.POST.get('new_phone')
        new_date = request.POST.get('new_date')

        get_task.fullname = new_fullname
        get_task.phone = new_phone
        get_task.date = new_date
        get_task.save()
        return redirect('appointment_update')

    else:
        context = {
            'get_task': get_task
        }
        return render(request, 'staff/update.html', context)


def staff_admin(request):
    return render(request)


def admin_department(request):
    doctor = Doctor.objects.all()
    department = Department.objects.all()
    return render(request, 'staff/department.html', {'department': department, 'doctor': doctor})



def to_bill(request):
    appointments = Appointment.objects.filter(is_completed=True, billed=False)
    billed = Appointment.objects.filter(billed=True)
    return render(request, 'staff/to_bill_table.html', {'appointments': appointments, 'billed': billed})


def billing(request, appointment_id):
    appointment = get_object_or_404(Appointment, pk=appointment_id)
    if request.method == 'POST':
        patient_name = appointment.first_name
        doctor_name = appointment.doctor
        appointment_quantity = int(request.POST.get('appointment_quantity'))
        service_quantity = int(request.POST.get('service_quantity'))
        payment_mode = request.POST.get('payment_mode')
        invoice = Invoice(
            patient=patient_name,
            doctor=doctor_name,
            appointment_quantity=appointment_quantity,
            service_quantity=service_quantity,
            payment_mode=payment_mode,
            appointment=appointment  # Assigning the appointment object
        )
        invoice.save()
        appointment.billed = True
        appointment.save()
        return redirect('to_bill')

    return render(request, 'staff/invoice.html', {'appointment': appointment})

