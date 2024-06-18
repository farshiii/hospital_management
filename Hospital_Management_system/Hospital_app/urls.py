from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('signin', views.signin, name='signin'),
    path('signup', views.signup, name='signup'),
    path('specialties', views.specialties, name='specialties'),
    path('message', views.message, name='message'),
    path('specialty/<int:Department_id>/', views.doctor_list_by_specialty, name='doctor_list_by_specialty'),
    path('user_logout', views.user_logout, name='logout'),
    path('appointment', views.appointment, name='appointment'),
    path('my-appointment', views.my_appointments, name='my-appointment'),
    path('appointment_full_view/<int:appointment_id>/', views.appointment_full_view, name='appointment_full_view'),
    path('invoice/<int:appointment_id>/', views.view_invoice, name='view_invoice'),
    # other url patterns

]
