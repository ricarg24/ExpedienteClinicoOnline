

from django.contrib import admin
from .models import Padre,Paciente,Aplicacionprocedimiento
from .models import Asignacionexamen,Cirugia,Cita,Consulta
from .models import Emergencia,Empleado,Enfermedad,\
    EnfermedadJoinConsulta,Especialidad,Examen,\
    Expediente,Ingreso,Medicamento,Medico,Menu
from .models import PacientePadeceEnfermedad,\
    PadrePadeceEnfermedad,Procedimiento,Realizacioncirugia,\
    Realizacionconsulta,RealizacionconsultaJoinCita
from .models import Recetamedica,Recursomultimedia,Responsable,\
    Rol,RolAccedeAMenu,Signosvitales,Tipoexamen,Tipomedicamento,\
    Tipoubicacion,Tratamiento
from .models import Ubicacion,Usuario
from . filter.padre_nombre import PadreNombreFilter
#clases para el filtrado
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('nombre1','nombre2','apellido1','apellido2','dui',)
    search_fields = ('dui',)
#agregado registros a la aplicacion

admin.site.register(Padre,CustomerAdmin)
admin.site.register(Paciente)
admin.site.register(Aplicacionprocedimiento)
admin.site.register(Asignacionexamen)
admin.site.register(Cirugia)
admin.site.register(Cita)
admin.site.register(Consulta)
admin.site.register(Emergencia)
admin.site.register(Empleado)
admin.site.register(Enfermedad)
admin.site.register(EnfermedadJoinConsulta)
admin.site.register(Especialidad)
admin.site.register(Examen)
admin.site.register(Expediente)
admin.site.register(Ingreso)
admin.site.register(Medicamento)
admin.site.register(Medico)
admin.site.register(Menu)
admin.site.register(PacientePadeceEnfermedad)
admin.site.register(PadrePadeceEnfermedad)
admin.site.register(Procedimiento)
admin.site.register(Realizacioncirugia)
admin.site.register(Realizacionconsulta)
admin.site.register(RealizacionconsultaJoinCita)
admin.site.register(Recetamedica)
admin.site.register(Recursomultimedia)
admin.site.register(Responsable)
admin.site.register(Rol)
admin.site.register(RolAccedeAMenu)
admin.site.register(Tipoubicacion)
admin.site.register(Signosvitales)
admin.site.register(Tipoexamen)
admin.site.register(Tipomedicamento)
admin.site.register(Tratamiento)
admin.site.register(Usuario)
admin.site.register(Ubicacion)
admin.site.site_header = 'Expediente Clinico Online Administracion'
admin.site.site_title = 'Expediente Clinico Online'
admin.site.index_title = 'Gestion Expediente Clinico Online'




