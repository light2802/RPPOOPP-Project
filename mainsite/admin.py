from django.contrib import admin
from .models import Patient, Hospital, Doctor, History


# Register your models here.

admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Hospital)
admin.site.register(History)