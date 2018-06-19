
#Ricardo Antonio Hernandez HG08008 BAD1152018

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
class PacienteAdmin(admin.ModelAdmin):
    list_display = ('nombre1','nombre2','apellido1','apellido2','dui','tel_fijo','id_responsable','id_expediente','id_usuario')
    search_fields = ('dui',)
admin.site.register(Paciente,PacienteAdmin)
class AplicacionprocedimientoAdmin(admin.ModelAdmin):
    list_display = ('id_procedimiento','id_expediente','id_tratamiento','dia_aplicacion_procedimiento',)
    search_fields = ('id_expediente',)
admin.site.register(Aplicacionprocedimiento,AplicacionprocedimientoAdmin)
class AsignacionexamenAdmin(admin.ModelAdmin):
    list_display = ('id_asignacion_examen','id_realizacion_consulta','id_ingreso','id_emergencia','resultado_obtenido','mes_asignacion_examen',)
    search_fields = ('id_asignacion_examen',)
admin.site.register(Asignacionexamen,AsignacionexamenAdmin)
class CirugiaAdmin(admin.ModelAdmin):
    list_display = ('codigo','nombre','costo',)
    search_fields = ('codigo',)
admin.site.register(Cirugia,CirugiaAdmin)
class CitaAdmin(admin.ModelAdmin):
    list_display = ('id_paciente','id_medico','id_ubicacion','dia','mes','anio','hora','minuto','estado',)
    search_fields = ('id_paciente',)
admin.site.register(Cita,CitaAdmin)
class ConsultaAdmin(admin.ModelAdmin):
    list_display = ('id_especialidad','codigo','nombre','costo',)
    search_fields = ('id_paciente',)
admin.site.register(Consulta,ConsultaAdmin)
class EmergenciaAdmin(admin.ModelAdmin):
    list_display = ('id_emergencia','id_medico','id_ubicacion','id_expediente','id_realizacion_consulta','sintomatologia_emergencia',
                    'dia_emergencia','mes_emergencia','anio_emergencia','hora_emergencia','minuto_emergencia',)
    search_fields = ('id_emergencia',)
admin.site.register(Emergencia,EmergenciaAdmin)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('id_empleado','id_usuario','nombre1','nombre2','apellido1','apellido2','dui','tel_movil',)
    search_fields = ('dui',)
admin.site.register(Empleado,EmpleadoAdmin)
class EnfermedadAdmin(admin.ModelAdmin):
    list_display = ('codigo_enfermedad','nombre_enfermedad',)
    search_fields = ('codigo_enfermedad',)
admin.site.register(Enfermedad,EnfermedadAdmin)
class EnfermedadJoinConsultaAdmin(admin.ModelAdmin):
    list_display = ('id_enfermedad','id_realizacion_consulta',)
    search_fields = ('id_realizacion_consulta',)
admin.site.register(EnfermedadJoinConsulta,EnfermedadJoinConsultaAdmin)
class EspecialidadAdmin(admin.ModelAdmin):
    list_display = ('codigo_especialidad','nombre_especialidad',)
    search_fields = ('codigo_especialidad',)
admin.site.register(Especialidad,EspecialidadAdmin)
class ExamenAdmin(admin.ModelAdmin):
    list_display = ('id_tipo_examen','codigo_examen','nombre_examen','costo_examen',)
    search_fields = ('codigo_examen',)
admin.site.register(Examen,ExamenAdmin)
class ExpedienteAdmin(admin.ModelAdmin):
    list_display = ('id_expediente','numero_expediente','id_paciente','dia_apertura_expediente','mes_apertura_expediente',
                    'dia_expiracion_expediente','mes_expiracion_expediente','anio_expiracion_expediente',)
    search_fields = ('numero_expediente',)
admin.site.register(Expediente,ExpedienteAdmin)
class IngresoAdmin(admin.ModelAdmin):
    list_display = ('id_expediente','id_paciente','id_realizacion_consulta',
                    'dia_inicio_ingreso','mes_inicio_ingreso','anio_inicio_ingreso',)
    search_fields = ('id_expediente',)
admin.site.register(Ingreso,IngresoAdmin)
class MedicamentoAdmin(admin.ModelAdmin):
    list_display = ('id_medicamento','id_tipo_medicamento','codigo_medicamento','nombre_medicamento','costo_medicamento',)
    search_fields = ('codigo_medicamento',)
admin.site.register(Medicamento,MedicamentoAdmin)
class MedicoAdmin(admin.ModelAdmin):
    list_display = ('id_medico','id_especialidad','id_empleado',)
    search_fields = ('id_medico',)
admin.site.register(Medico,MedicoAdmin)
class PacientePadeceEnfermedadAdmin(admin.ModelAdmin):
    list_display = ('id_enfermedad','id_paciente',)
    search_fields = ('id_paciente',)
admin.site.register(PacientePadeceEnfermedad,PacientePadeceEnfermedadAdmin)
class ProcedimientoAdmin(admin.ModelAdmin):
    list_display = ('id_procedimiento','nombre_procedimiento','codigo_procedimiento','costo_procedimiento',)
    search_fields = ('codigo_procedimiento',)
admin.site.register(Procedimiento,ProcedimientoAdmin)
class RealizacioncirugiaAdmin(admin.ModelAdmin):
    list_display = ('id_realizacion_cirugia','id_medico','id_ubicacion','id_expediente','id_cita',
                    'id_realizacion_consulta','id_cirugia','dia_realizacion_cirugia',
                    'mes_realizacion_cirugia','anio_realizacion_cirugia',)
    search_fields = ('id_expediente',)
admin.site.register(Realizacioncirugia,RealizacioncirugiaAdmin)
class RealizacionconsultaAdmin(admin.ModelAdmin):
    list_display = ('id_realizacion_consulta','id_expediente','id_emergencia','id_ingreso','id_consulta',)
    search_fields = ('id_expediente',)
admin.site.register(Realizacionconsulta,RealizacionconsultaAdmin)
class RealizacionconsultaJoinCitaAdmin(admin.ModelAdmin):
    list_display = ('id_cita','id_realizacion_consulta',)
    search_fields = ('id_cita',)
admin.site.register(RealizacionconsultaJoinCita,RealizacionconsultaJoinCitaAdmin)
class RecetamedicaAdmin(admin.ModelAdmin):
    list_display = ('id_tratamiento','id_medicamento','dosis','frecuencia',)
    search_fields = ('id_tratamiento',)
admin.site.register(Recetamedica,RecetamedicaAdmin)
class RecursomultimediaAdmin(admin.ModelAdmin):
    list_display = ('id_recurso_multimedia','id_procedimiento','id_examen','data','contentype',)
    search_fields = ('id_tratamiento',)
admin.site.register(Recursomultimedia,RecursomultimediaAdmin)
class ResponsableAdmin(admin.ModelAdmin):
    list_display = ('nombre1','nombre2','apellido1','apellido2',)
    search_fields = ('dui',)
admin.site.register(Responsable,ResponsableAdmin)
admin.site.register(Tipoubicacion)
class SignosvitalesAdmin(admin.ModelAdmin):
    list_display = ('id_expediente','temperatura','estatura','dia','mes','anio',)
    search_fields = ('id_expediente',)
admin.site.register(Signosvitales,SignosvitalesAdmin)
class TipoexamenAdmin(admin.ModelAdmin):
    list_display = ('codigo_tipo_examen','nombre_tipo_examen',)
    search_fields = ('id_tipo_examen',)
admin.site.register(Tipoexamen,TipoexamenAdmin)
class TipomedicamentoAdmin(admin.ModelAdmin):
    list_display = ('id_tipo_medicamento','presentacion',)
    search_fields = ('id_tipo_medicamento',)
admin.site.register(Tipomedicamento,TipomedicamentoAdmin)
class TratamientoAdmin(admin.ModelAdmin):
    list_display = ('id_realizacion_consulta','recomendaciones',)
    search_fields = ('id_tratamiento',)
admin.site.register(Tratamiento,TratamientoAdmin)
admin.site.register(Usuario)
class UbicacionAdmin(admin.ModelAdmin):
    list_display = ('id_tipo_ubicacion','codigo_ubicacion','nombre_ubicacion',)
    search_fields = ('id_tratamiento',)
admin.site.register(Ubicacion,UbicacionAdmin)
admin.site.site_header = 'Expediente Clinico Online Administracion'
admin.site.site_title = 'Expediente Clinico Online'
admin.site.index_title = 'Gestion Expediente Clinico Online'




