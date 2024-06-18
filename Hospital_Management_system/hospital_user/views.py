from django.shortcuts import render


def admin_login(request):
    return render(request, 'admin_panel/admin_login.html')


def staff_reg(request):
    return render(request, 'admin_panel/staff_registration.html')
