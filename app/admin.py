from django.contrib import admin
from app.models import Doctor, patient, Medicine

# Register your models here.

admin.site.register(Doctor)
admin.site.register(patient)
admin.site.register(Medicine)
