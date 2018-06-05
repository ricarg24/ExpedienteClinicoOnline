

from django.contrib import admin
from .models import Padre,Paciente,Aplicacionprocedimiento



admin.site.register(Padre)
admin.site.register(Paciente)
admin.site.register(Aplicacionprocedimiento)



admin.site.site_header = 'Expediente Clinico Online Administracion'
admin.site.site_title = 'Expediente Clinico Online'
admin.site.index_title = 'Gestion Expediente Clinico Online'




