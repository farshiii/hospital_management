from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from hospital_staff.models import Invoice
from .forms import AppointmentForm, MessageForm
from django.contrib.auth import logout as auth_logout
from hospital_admin.models import Doctor, Department
from .models import Appointment


# Create your views here.


def home(request):
    department = Department.objects.all()
    return render(request, 'index.html', {'department': department})


def dashboard(request):

    return render(request, 'signup.html')


def signup(request):

    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email_up']
        password = request.POST['password']

        myuser = User.objects.create_user(username, email, password)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        return redirect('signin')

    return render(request, 'signin.html')


def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            first_name = user.first_name
            print(first_name)
            return render(request, 'index.html', {'first_name': first_name})
        else:
            messages.error(request, "Invalid Credentials")

    return render(request, 'signin.html')


def user_logout(request):
    auth_logout(request)  # Logging out the currently authenticated user
    return redirect('home')  # Redirecting to the login page

@login_required(login_url='signup')
def appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)  # Don't save yet
            appointment.user = request.user       # Set the user
            appointment.save()
            # Redirect to a success page or display a success message
            return redirect('home')
    else:
        form = AppointmentForm()

    doctor = Doctor.objects.all()
    department = Department.objects.all()
    return render(request, 'appointment.html', {'form': form, 'department': department, 'doctor': doctor})


def message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.user = request.user
            message.save()

        else:
            form = MessageForm()

    return render(request, 'index.html', {'form': form})


def specialties(request):
    department = Department.objects.all()
    return render(request, 'Main/spacialties.html', {'department': department})


def doctor_list_by_specialty(request, Department_id):
    department = get_object_or_404(Department, id=Department_id)
    Doctors = Doctor.objects.filter(department=department)
    return render(request, 'main/doctor_list.html', {'department': department, 'Doctors': Doctors})


@login_required
def my_appointments(request):
    user = request.user
    appointment = Appointment.objects.filter(user=user)
    return render(request, 'my_appointments.html', {'appointment': appointment})


def appointment_full_view(request, appointment_id):
    appointment = get_object_or_404(Appointment, pk=appointment_id)
    try:
        invoice = Invoice.objects.get(appointment=appointment)
    except Invoice.DoesNotExist:
        invoice = None

    return render(request, 'user_appointment_fullview.html', {'appointment': appointment, 'invoice': invoice})


def view_invoice(request, appointment_id):
    appointment = get_object_or_404(Appointment, pk=appointment_id)
    try:
        invoice = Invoice.objects.get(appointment=appointment)
    except Invoice.DoesNotExist:
        invoice = None

    return render(request, 'invoice.html', {'appointment': appointment, 'invoice': invoice})
