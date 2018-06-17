

from django.contrib import admin
from .models import Padre,Paciente,Aplicacionprocedimiento
from . filter.padre_nombre import PadreNombreFilter




class CustomerAdmin(admin.ModelAdmin):
    list_display = ('nombre1','nombre2','apellido1','apellido2','dui',)
    search_fields = ('dui',)


admin.site.register(Padre,CustomerAdmin)
admin.site.register(Paciente)
admin.site.register(Aplicacionprocedimiento)




admin.site.site_header = 'Expediente Clinico Online Administracion'
admin.site.site_title = 'Expediente Clinico Online'
admin.site.index_title = 'Gestion Expediente Clinico Online'




