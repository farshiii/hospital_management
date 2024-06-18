from django.urls import path, include
from . import views


urlpatterns = [
    path('staff', views.admin_home, name='staff_home'),
    path('appointment_by_staff', views.appointment_by_staff, name='appointment_staff'),
    path('_admin_department', views.admin_department, name='admin_department'),
    path('completed_appointment', views.completed_appointment, name='completed_appointment'),
    path('pending_appointment', views.pending_appointment, name='pending_appointment'),
    path('appointment_update', views.appointment_update, name='appointment_update'),
    path('update_task/<int:update_id>/', views.update_task, name='update_task'),
    path('delete_task/<int:delete_id>/', views.delete_task, name='delete_task'),
    path('mark_as_done/<int:task_id>/', views.mark_as_done, name='mark_as_done'),
    path('mark_as_undone/<int:task_id>/', views.mark_as_undone, name='mark_as_undone'),
    path('cancel/<int:task_id>/', views.mark_as_cancel, name='cancel'),
    path('mark_as_un_cancel/<int:task_id>/', views.mark_as_un_cancel, name='mark_as_un_cancel'),
    path('billing/<int:appointment_id>/', views.billing, name='billing'),
    path('to_bill', views.to_bill, name='to_bill'),
    path('staff_login', views.staff_login, name='staff_login'),
    ]
