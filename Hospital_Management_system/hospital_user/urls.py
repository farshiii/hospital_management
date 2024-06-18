from django.urls import path, include
from . import views


urlpatterns = [
    path('admin_login', views.admin_login, name='admin_login'),
    path('staff_reg', views.staff_reg, name='staff_reg'),
    path('staff_login',views.staff_login, name=staff_login),

    ]
