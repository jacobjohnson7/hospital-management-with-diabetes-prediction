from django.urls import path
from app import views

urlpatterns = [
    path('', views.home, name='home'),
    path('patientregister',views.patientregister, name='patientregister'),
    path('patientlogin', views.patientlogin, name='patientlogin'),
    path('doc', views.doc, name='doc'),
    path('formm', views.formm, name='formm'),
    path('patient-management', views.patient_management, name='patient_management'),
    path('delete/<int:id>/', views.delete_patient, name='delete_patient'),
    path('logout/', views.logout, name='logout'),
    path('check-diabetes/', views.check_diabetes, name='check_diabetes'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('contact/', views.contact, name='contact'),
    path('doctorlogin/', views.doctorlogin, name='doctorlogin'),
    path('doctordashboard/', views.doctordashboard, name='doctordashboard'),
    path('pharmacy/', views.pharmacy, name='pharmacy'),
    path('adminlogin/', views.adminlogin, name='adminlogin'),
    path('admindashboard/', views.admindashboard, name='admindashboard'),
    path('adminlogout/', views.adminlogout, name='adminlogout'),
]