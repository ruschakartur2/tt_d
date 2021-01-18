from django.contrib import admin

# Register your models here.
from pations.models import Diagnos, Patient

admin.site.register(Diagnos)
admin.site.register(Patient)