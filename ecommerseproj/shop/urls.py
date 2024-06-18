
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/',views.signup, name='signup'),
    path('signin/',views.signin, name='signin'),
    path('signout/',views.signout, name='signout'),

    path('about/', views.about, name='support'),
    path('product/', views.product, name='product'),
    path('<slug:slug_c>/', views.home, name="by_department"),
    path('<slug:slug_c>/<slug_p>/', views.doc_details, name="by_doctor"),

]
