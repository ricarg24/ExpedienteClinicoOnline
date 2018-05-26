# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Aplicacionprocedimiento(models.Model):
    id_procedimiento = models.ForeignKey('Procedimiento', models.DO_NOTHING, db_column='id_procedimiento', blank=True, null=True)
    id_expediente = models.ForeignKey('Expediente', models.DO_NOTHING, db_column='id_expediente', blank=True, null=True)
    id_tratamiento = models.ForeignKey('Tratamiento', models.DO_NOTHING, db_column='id_tratamiento', blank=True, null=True)
    dia_aplicacion_procedimiento = models.IntegerField(blank=True, null=True)
    mes_aplicacion_procedimienot = models.IntegerField(blank=True, null=True)
    anio_aplicacion_procedimiento = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aplicacionprocedimiento'


class Asignacionexamen(models.Model):
    id_asignacion_examen = models.AutoField(primary_key=True)
    id_realizacion_consulta = models.ForeignKey('Realizacionconsulta', models.DO_NOTHING, db_column='id_realizacion_consulta', blank=True, null=True)
    id_ingreso = models.ForeignKey('Ingreso', models.DO_NOTHING, db_column='id_ingreso', blank=True, null=True)
    id_emergencia = models.ForeignKey('Emergencia', models.DO_NOTHING, db_column='id_emergencia', blank=True, null=True)
    id_examen = models.ForeignKey('Examen', models.DO_NOTHING, db_column='id_examen', blank=True, null=True)
    resultado_obtenido = models.TextField(blank=True, null=True)
    dia_asignacion_examen = models.IntegerField(blank=True, null=True)
    mes_asignacion_examen = models.IntegerField(blank=True, null=True)
    anio_asignacion_examen = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'asignacionexamen'


class Cirugia(models.Model):
    id_especialidad = models.ForeignKey('Especialidad', models.DO_NOTHING, db_column='id_especialidad', blank=True, null=True)
    codigo = models.CharField(max_length=15, blank=True, null=True)
    nombre = models.CharField(max_length=30, blank=True, null=True)
    costo = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cirugia'


class Cita(models.Model):
    id_paciente = models.IntegerField(blank=True, null=True)
    id_medico = models.IntegerField(blank=True, null=True)
    id_ubicacion = models.ForeignKey('Ubicacion', models.DO_NOTHING, db_column='id_ubicacion', blank=True, null=True)
    id_realizacion_cirugia = models.ForeignKey('Realizacioncirugia', models.DO_NOTHING, db_column='id_realizacion_cirugia', blank=True, null=True)
    dia = models.IntegerField(blank=True, null=True)
    mes = models.IntegerField(blank=True, null=True)
    anio = models.IntegerField(blank=True, null=True)
    hora = models.IntegerField(blank=True, null=True)
    minuto = models.IntegerField(blank=True, null=True)
    estado = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cita'


class Consulta(models.Model):
    id_especialidad = models.ForeignKey('Especialidad', models.DO_NOTHING, db_column='id_especialidad', blank=True, null=True)
    codigo = models.CharField(max_length=15, blank=True, null=True)
    nombre = models.CharField(max_length=30, blank=True, null=True)
    costo = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'consulta'


class Emergencia(models.Model):
    id_emergencia = models.AutoField(primary_key=True)
    id_medico = models.IntegerField(blank=True, null=True)
    id_ubicacion = models.ForeignKey('Ubicacion', models.DO_NOTHING, db_column='id_ubicacion', blank=True, null=True)
    id_expediente = models.ForeignKey('Expediente', models.DO_NOTHING, db_column='id_expediente', blank=True, null=True)
    id_realizacion_consulta = models.ForeignKey('Realizacionconsulta', models.DO_NOTHING, db_column='id_realizacion_consulta', blank=True, null=True)
    sintomatologia_emergencia = models.TextField(blank=True, null=True)
    dia_emergencia = models.IntegerField(blank=True, null=True)
    mes_emergencia = models.IntegerField(blank=True, null=True)
    anio_emergencia = models.IntegerField(blank=True, null=True)
    hora_emergencia = models.IntegerField(blank=True, null=True)
    minuto_emergencia = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'emergencia'


class Empleado(models.Model):
    id_empleado = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_usuario')
    nombre1 = models.CharField(max_length=20)
    nombre2 = models.CharField(max_length=20, blank=True, null=True)
    apellido1 = models.CharField(max_length=20)
    apellido2 = models.CharField(max_length=20, blank=True, null=True)
    pais = models.CharField(max_length=15)
    division = models.CharField(max_length=15)
    subdivision = models.CharField(max_length=15, blank=True, null=True)
    tel_fijo = models.CharField(max_length=15)
    tel_movil = models.CharField(max_length=15, blank=True, null=True)
    email = models.CharField(max_length=40, blank=True, null=True)
    dui = models.CharField(unique=True, max_length=15)
    apellido_casada = models.CharField(max_length=20, blank=True, null=True)
    codigo_empleado = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'empleado'


class Enfermedad(models.Model):
    id_enfermedad = models.AutoField(primary_key=True)
    codigo_enfermedad = models.CharField(max_length=15, blank=True, null=True)
    nombre_enfermedad = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'enfermedad'


class EnfermedadJoinConsulta(models.Model):
    id_enfermedad = models.ForeignKey(Enfermedad, models.DO_NOTHING, db_column='id_enfermedad', primary_key=True)
    id_realizacion_consulta = models.ForeignKey('Realizacionconsulta', models.DO_NOTHING, db_column='id_realizacion_consulta')

    class Meta:
        managed = False
        db_table = 'enfermedad_join_consulta'
        unique_together = (('id_enfermedad', 'id_realizacion_consulta'), ('id_enfermedad', 'id_realizacion_consulta'),)


class Especialidad(models.Model):
    id_especialidad = models.AutoField(primary_key=True)
    codigo_especialidad = models.CharField(max_length=15, blank=True, null=True)
    nombre_especialidad = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'especialidad'


class Examen(models.Model):
    id_examen = models.AutoField(primary_key=True)
    id_tipo_examen = models.ForeignKey('Tipoexamen', models.DO_NOTHING, db_column='id_tipo_examen', blank=True, null=True)
    codigo_examen = models.CharField(max_length=15, blank=True, null=True)
    nombre_examen = models.CharField(max_length=50, blank=True, null=True)
    costo_examen = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'examen'


class Expediente(models.Model):
    id_expediente = models.AutoField(primary_key=True)
    id_paciente = models.IntegerField()
    dia_apertura_expediente = models.IntegerField(blank=True, null=True)
    mes_apertura_expediente = models.IntegerField(blank=True, null=True)
    anio_apertura_expediente = models.IntegerField(blank=True, null=True)
    dia_expiracion_expediente = models.IntegerField(blank=True, null=True)
    mes_expiracion_expediente = models.IntegerField(blank=True, null=True)
    anio_expiracion_expediente = models.IntegerField(blank=True, null=True)
    numero_expediente = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'expediente'


class Ingreso(models.Model):
    id_ingreso = models.AutoField(primary_key=True)
    id_paciente = models.IntegerField(blank=True, null=True)
    id_medico = models.IntegerField(blank=True, null=True)
    id_ubicacion = models.ForeignKey('Ubicacion', models.DO_NOTHING, db_column='id_ubicacion', blank=True, null=True)
    id_expediente = models.ForeignKey(Expediente, models.DO_NOTHING, db_column='id_expediente', blank=True, null=True)
    id_realizacion_consulta = models.ForeignKey('Realizacionconsulta', models.DO_NOTHING, db_column='id_realizacion_consulta', blank=True, null=True)
    dia_inicio_ingreso = models.IntegerField(blank=True, null=True)
    mes_inicio_ingreso = models.IntegerField(blank=True, null=True)
    anio_inicio_ingreso = models.IntegerField(blank=True, null=True)
    dia_fin_ingreso = models.IntegerField(blank=True, null=True)
    mes_fin_ingreso = models.IntegerField(blank=True, null=True)
    anio_fin_ingreso = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ingreso'


class Medicamento(models.Model):
    id_medicamento = models.AutoField(primary_key=True)
    id_tipo_medicamento = models.ForeignKey('Tipomedicamento', models.DO_NOTHING, db_column='id_tipo_medicamento', blank=True, null=True)
    codigo_medicamento = models.CharField(max_length=15, blank=True, null=True)
    nombre_medicamento = models.CharField(max_length=50, blank=True, null=True)
    costo_medicamento = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'medicamento'


class Medico(models.Model):
    id_medico = models.AutoField(primary_key=True)
    id_especialidad = models.ForeignKey(Especialidad, models.DO_NOTHING, db_column='id_especialidad')
    id_empleado = models.ForeignKey(Empleado, models.DO_NOTHING, db_column='id_empleado')

    class Meta:
        managed = False
        db_table = 'medico'


class Menu(models.Model):
    id_menu = models.AutoField(primary_key=True)
    icono = models.CharField(max_length=40, blank=True, null=True)
    titulo = models.CharField(max_length=25, blank=True, null=True)
    url = models.CharField(max_length=250, blank=True, null=True)
    recurso = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'menu'


class Paciente(models.Model):
    id_paciente = models.AutoField(primary_key=True)
    id_responsable = models.ForeignKey('Responsable', models.DO_NOTHING, db_column='id_responsable')
    id_expediente = models.ForeignKey(Expediente, models.DO_NOTHING, db_column='id_expediente', blank=True, null=True)
    id_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_usuario', blank=True, null=True)
    estado_civil_paciente = models.IntegerField(blank=True, null=True)
    apellido_casado_paciente = models.CharField(max_length=20, blank=True, null=True)
    dia_nacimiento_paciente = models.IntegerField(blank=True, null=True)
    mes_nacimiento_paciente = models.IntegerField(blank=True, null=True)
    anio_nacimiento_paciente = models.IntegerField(blank=True, null=True)
    id_padre = models.ForeignKey('Padre', models.DO_NOTHING, db_column='id_padre', blank=True, null=True)
    id_madre = models.ForeignKey('Padre', models.DO_NOTHING, db_column='id_madre', blank=True, null=True)
    nombre1 = models.CharField(max_length=20)
    nombre2 = models.CharField(max_length=20)
    apellido1 = models.CharField(max_length=20)
    apellido2 = models.CharField(max_length=20, blank=True, null=True)
    pais = models.CharField(max_length=15, blank=True, null=True)
    division = models.CharField(max_length=15, blank=True, null=True)
    subdivision = models.CharField(max_length=15, blank=True, null=True)
    tel_fijo = models.CharField(max_length=15, blank=True, null=True)
    tel_movil = models.CharField(max_length=15, blank=True, null=True)
    email = models.CharField(max_length=40, blank=True, null=True)
    dui = models.CharField(unique=True, max_length=15, blank=True, null=True)
    genero = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'paciente'


class PacientePadeceEnfermedad(models.Model):
    id_enfermedad = models.ForeignKey(Enfermedad, models.DO_NOTHING, db_column='id_enfermedad', primary_key=True)
    id_paciente = models.ForeignKey(Paciente, models.DO_NOTHING, db_column='id_paciente')

    class Meta:
        managed = False
        db_table = 'paciente_padece_enfermedad'
        unique_together = (('id_enfermedad', 'id_paciente'),)


class Padre(models.Model):
    id_padre = models.AutoField(primary_key=True)
    nombre1 = models.CharField(max_length=20)
    nombre2 = models.CharField(max_length=20)
    apellido1 = models.CharField(max_length=20)
    apellido2 = models.CharField(max_length=20, blank=True, null=True)
    pais = models.CharField(max_length=15)
    division = models.CharField(max_length=15)
    subdivision = models.CharField(max_length=15, blank=True, null=True)
    dui = models.CharField(unique=True, max_length=15)
    genero = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'padre'


class PadrePadeceEnfermedad(models.Model):
    id_enfermedad = models.ForeignKey(Enfermedad, models.DO_NOTHING, db_column='id_enfermedad', primary_key=True)
    id_padre = models.ForeignKey(Padre, models.DO_NOTHING, db_column='id_padre')

    class Meta:
        managed = False
        db_table = 'padre_padece_enfermedad'
        unique_together = (('id_enfermedad', 'id_padre'),)


class Procedimiento(models.Model):
    id_procedimiento = models.AutoField(primary_key=True)
    nombre_procedimiento = models.CharField(max_length=50, blank=True, null=True)
    codigo_procedimiento = models.CharField(max_length=15, blank=True, null=True)
    costo_procedimiento = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'procedimiento'


class Realizacioncirugia(models.Model):
    id_realizacion_cirugia = models.AutoField(primary_key=True)
    id_medico = models.IntegerField(blank=True, null=True)
    id_ubicacion = models.ForeignKey('Ubicacion', models.DO_NOTHING, db_column='id_ubicacion', blank=True, null=True)
    id_expediente = models.ForeignKey(Expediente, models.DO_NOTHING, db_column='id_expediente', blank=True, null=True)
    id_cita = models.ForeignKey(Cita, models.DO_NOTHING, db_column='id_cita', blank=True, null=True)
    id_realizacion_consulta = models.ForeignKey('Realizacionconsulta', models.DO_NOTHING, db_column='id_realizacion_consulta', blank=True, null=True)
    id_cirugia = models.ForeignKey(Cirugia, models.DO_NOTHING, db_column='id_cirugia', blank=True, null=True)
    dia_realizacion_cirugia = models.IntegerField(blank=True, null=True)
    mes_realizacion_cirugia = models.IntegerField(blank=True, null=True)
    anio_realizacion_cirugia = models.IntegerField(blank=True, null=True)
    hora_inicio_realizacion_cirugia = models.IntegerField(blank=True, null=True)
    min_inicio_realizacion_cirugia = models.IntegerField(blank=True, null=True)
    hora_fin_realizacion_cirugia = models.IntegerField(blank=True, null=True)
    minuto_fin_realizacion_cirugia = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'realizacioncirugia'


class Realizacionconsulta(models.Model):
    id_realizacion_consulta = models.AutoField(primary_key=True)
    id_expediente = models.ForeignKey(Expediente, models.DO_NOTHING, db_column='id_expediente', blank=True, null=True)
    id_emergencia = models.ForeignKey(Emergencia, models.DO_NOTHING, db_column='id_emergencia', blank=True, null=True)
    id_ingreso = models.ForeignKey(Ingreso, models.DO_NOTHING, db_column='id_ingreso', blank=True, null=True)
    id_consulta = models.ForeignKey(Consulta, models.DO_NOTHING, db_column='id_consulta', blank=True, null=True)
    observacones = models.CharField(max_length=1000, blank=True, null=True)
    sintom_realizacion_consulta = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'realizacionconsulta'


class RealizacionconsultaJoinCita(models.Model):
    id_cita = models.ForeignKey(Cita, models.DO_NOTHING, db_column='id_cita', primary_key=True)
    id_realizacion_consulta = models.ForeignKey(Realizacionconsulta, models.DO_NOTHING, db_column='id_realizacion_consulta')

    class Meta:
        managed = False
        db_table = 'realizacionconsulta_join_cita'
        unique_together = (('id_cita', 'id_realizacion_consulta'), ('id_cita', 'id_realizacion_consulta'),)


class Recetamedica(models.Model):
    id_receta_medica = models.AutoField(primary_key=True)
    id_tratamiento = models.ForeignKey('Tratamiento', models.DO_NOTHING, db_column='id_tratamiento', blank=True, null=True)
    id_medicamento = models.ForeignKey(Medicamento, models.DO_NOTHING, db_column='id_medicamento', blank=True, null=True)
    dosis = models.CharField(max_length=15, blank=True, null=True)
    frecuencia = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'recetamedica'


class Recursomultimedia(models.Model):
    id_recurso_multimedia = models.AutoField(primary_key=True)
    id_procedimiento = models.ForeignKey(Procedimiento, models.DO_NOTHING, db_column='id_procedimiento', blank=True, null=True)
    id_examen = models.ForeignKey(Examen, models.DO_NOTHING, db_column='id_examen', blank=True, null=True)
    data = models.BinaryField(blank=True, null=True)
    contentype = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'recursomultimedia'


class Responsable(models.Model):
    nombre1 = models.CharField(max_length=20)
    nombre2 = models.CharField(max_length=20)
    apellido1 = models.CharField(max_length=20)
    apellido2 = models.CharField(max_length=20, blank=True, null=True)
    pais = models.CharField(max_length=15)
    division = models.CharField(max_length=15)
    subdivision = models.CharField(max_length=15, blank=True, null=True)
    tel_fijo = models.CharField(max_length=15, blank=True, null=True)
    tel_cel = models.CharField(max_length=15, blank=True, null=True)
    id_responsable = models.AutoField(primary_key=True)
    dui = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'responsable'


class Rol(models.Model):
    id_rol = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20, blank=True, null=True)
    descripcion = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rol'


class RolAccedeAMenu(models.Model):
    id_menu = models.ForeignKey(Menu, models.DO_NOTHING, db_column='id_menu', primary_key=True)
    id_rol = models.ForeignKey(Rol, models.DO_NOTHING, db_column='id_rol')
    orden = models.IntegerField(blank=True, null=True)
    add = models.NullBooleanField()
    edit = models.NullBooleanField()
    list = models.NullBooleanField()
    del_field = models.NullBooleanField(db_column='del')  # Field renamed because it was a Python reserved word.

    class Meta:
        managed = False
        db_table = 'rol_accede_a_menu'
        unique_together = (('id_menu', 'id_rol'), ('id_menu', 'id_rol'),)


class Signosvitales(models.Model):
    peso = models.FloatField()
    temperatura = models.FloatField(blank=True, null=True)
    estatura = models.FloatField()
    presion_arterial = models.FloatField(blank=True, null=True)
    ritmo_cardiaco = models.FloatField(blank=True, null=True)
    dia = models.IntegerField()
    mes = models.IntegerField()
    anio = models.IntegerField()
    id_expediente = models.ForeignKey(Expediente, models.DO_NOTHING, db_column='id_expediente')

    class Meta:
        managed = False
        db_table = 'signosvitales'


class Tipoexamen(models.Model):
    id_tipo_examen = models.AutoField(primary_key=True)
    nombre_tipo_examen = models.CharField(max_length=50, blank=True, null=True)
    codigo_tipo_examen = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipoexamen'


class Tipomedicamento(models.Model):
    id_tipo_medicamento = models.AutoField(primary_key=True)
    presentacion = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'tipomedicamento'


class Tipoubicacion(models.Model):
    id_tipo_ubicacion = models.AutoField(primary_key=True)
    nombre_tipo_ubicacion = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipoubicacion'


class Tratamiento(models.Model):
    id_tratamiento = models.AutoField(primary_key=True)
    id_realizacion_consulta = models.ForeignKey(Realizacionconsulta, models.DO_NOTHING, db_column='id_realizacion_consulta', blank=True, null=True)
    recomendaciones = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tratamiento'


class Ubicacion(models.Model):
    id_ubicacion = models.AutoField(primary_key=True)
    id_tipo_ubicacion = models.ForeignKey(Tipoubicacion, models.DO_NOTHING, db_column='id_tipo_ubicacion', blank=True, null=True)
    codigo_ubicacion = models.CharField(max_length=15, blank=True, null=True)
    nivel = models.IntegerField(blank=True, null=True)
    numero = models.IntegerField(blank=True, null=True)
    nombre_ubicacion = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ubicacion'


class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    id_rol = models.ForeignKey(Rol, models.DO_NOTHING, db_column='id_rol', blank=True, null=True)
    username = models.CharField(max_length=25)
    password = models.CharField(max_length=50)
    estado = models.BooleanField()
    last_login = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usuario'
