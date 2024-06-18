from django.urls import path, include
from . import views

urlpatterns = [
    path('Admin_home',views.admin_home, name='admin_home'),
    path('Appointment_dash/', views.analytics_view, name='Appointment_dash'),
    path('adddoctor', views.adddoctor, name='adddoctor'),
    path('adddepartment', views.adddepartment, name='adddepartment'),
    path('Profit_dash/', views.plot_appointments, name='Profit_dash'),
    path('admin_staff_page/', views.admin_staff_page, name='admin_staff_page')
    # path('<slug:slug_c>/', views.doc_details, name="product_by_category"),
    # path('<slug:slug_c>/<slug_p>/', views.doc_details, name="product_det"),

]
