# -*- coding: utf-8 -*-

# Librerias/Clases Python
from __future__ import unicode_literals

# Librerias/Clases Django
from django.db import models


class VIEW_EMPLEADOS_SIMPLE(models.Model):
    pers_clave = models.IntegerField(primary_key=True)
    pers_tipo_codigo = models.IntegerField()
    pers_tipo_desc = models.CharField(max_length=80)
    pers_empleado_numero = models.CharField(max_length=30)
    pers_titulo = models.CharField(max_length=30)
    pers_primer_nombre = models.CharField(max_length=150)
    pers_segundo_nombre = models.CharField(max_length=60)
    pers_apellido_paterno = models.CharField(max_length=150)
    pers_apellido_materno = models.CharField(max_length=150)
    pers_nombre_completo = models.CharField(max_length=240)
    pers_genero_clave = models.CharField(max_length=30)
    pers_genero_desc = models.CharField(max_length=11)
    pers_curp = models.CharField(max_length=30)
    pers_nacionalidad_clave = models.CharField(max_length=30)
    pers_rfc = models.CharField(max_length=150)
    pers_numero_imss = models.CharField(max_length=150)
    pers_ife = models.CharField(max_length=150)
    pers_fecha_nacimiento = models.CharField(max_length=8)
    pers_ciudad_nacimiento = models.CharField(max_length=90)
    pers_estado_nacimiento = models.CharField(max_length=90)
    pers_pais_nacimiento_clave = models.CharField(max_length=90)
    pers_fecha_efective_desde = models.CharField(max_length=8)
    pers_fecha_efective_hasta = models.CharField(max_length=8)
    pers_email = models.CharField(max_length=240)
    pers_estado_civil = models.CharField(max_length=30)
    pers_estado_civil_desc = models.CharField(max_length=7)
    pers_fecha_contratacion = models.CharField(max_length=8)

    class Meta:
        managed = False
        db_table = u'"NUVAPP"."VIEW_EMPLEADOS_SIMPLE"'


class VIEW_EMPLEADOS_GRADO(models.Model):
    pers_clave = models.IntegerField(primary_key=True)
    pers_empleado_numero = models.CharField(max_length=30)
    pers_nombre_completo = models.CharField(max_length=240)
    asig_puesto_desc = models.CharField(max_length=240)
    asig_organizacion_id = models.IntegerField()
    asig_organizacion_desc = models.CharField(max_length=240)
    qua_grado_academico = models.CharField(max_length=240)
    qua_ultimo_estudio = models.CharField(max_length=240)
    qua_especialidad = models.CharField(max_length=240)
    qua_version_num = models.IntegerField()

    class Meta:
        managed = False
        db_table = u'"NUVAPP"."VIEW_EMPLEADOS_GRADO"'


class VIEW_EMPLEADOS_FULL(models.Model):
    pers_clave = models.IntegerField(primary_key=True)
    pers_tipo_codigo = models.IntegerField()
    pers_tipo_desc = models.CharField(max_length=80)
    pers_empleado_numero = models.CharField(max_length=30)
    pers_titulo = models.CharField(max_length=30)
    pers_primer_nombre = models.CharField(max_length=150)
    pers_segundo_nombre = models.CharField(max_length=60)
    pers_apellido_paterno = models.CharField(max_length=150)
    pers_apellido_materno = models.CharField(max_length=150)
    pers_nombre_completo = models.CharField(max_length=240)
    pers_genero_clave = models.CharField(max_length=30)
    pers_genero_desc = models.CharField(max_length=11)
    pers_curp = models.CharField(max_length=30)
    pers_nacionalidad_clave = models.CharField(max_length=30)
    pers_rfc = models.CharField(max_length=150)
    pers_numero_imss = models.CharField(max_length=150)
    pers_ife = models.CharField(max_length=150)
    pers_fecha_nacimiento = models.DateField(max_length=8)
    pers_ciudad_nacimiento = models.CharField(max_length=90)
    pers_estado_nacimiento = models.CharField(max_length=90)
    pers_pais_nacimiento_clave = models.CharField(max_length=90)
    pers_fecha_efective_desde = models.CharField(max_length=8)
    pers_fecha_efective_hasta = models.CharField(max_length=8)
    pers_email = models.CharField(max_length=240)
    pers_estado_civil = models.CharField(max_length=30)
    pers_estado_civil_desc = models.CharField(max_length=7)
    pers_fecha_contratacion = models.DateField()
    asig_clave = models.IntegerField()
    asig_empleado_numero = models.CharField(max_length=30)
    asig_persona_clave = models.IntegerField()
    asig_fecha_inicio = models.DateField()
    asig_fecha_fin = models.DateField()
    asig_organizacion_clave = models.IntegerField()
    asig_organizacion_desc = models.CharField(max_length=240)
    asig_trabajo_clave = models.IntegerField()
    asig_trabajo_desc = models.CharField(max_length=700)
    asig_grado_clave = models.IntegerField()
    asig_grado_desc = models.CharField(max_length=240)
    asig_ubicacion_clave = models.IntegerField()
    asig_ubicacion_desc = models.CharField(max_length=60)
    asig_grupo_clave = models.IntegerField()
    asig_grupo_desc = models.CharField(max_length=240)
    asig_puesto_clave = models.IntegerField()
    asig_puesto_desc = models.CharField(max_length=240)
    asig_nomina_clave = models.IntegerField()
    asig_nomina_desc = models.CharField(max_length=80)
    asig_estado_clave = models.IntegerField()
    asig_estado_desc = models.CharField(max_length=80)
    asig_categoria_codigo = models.CharField(max_length=30)
    asig_salario_base_clave = models.IntegerField()
    asig_salario_base_desc = models.CharField(max_length=30)
    informacion_estatutaria_clave = models.IntegerField()
    informacion_estatutaria_desc = models.CharField(max_length=700)
    asig_version = models.IntegerField()
    asig_jefe_directo_clave = models.IntegerField()
    asig_jefe_directo_desc = models.CharField(max_length=240)
    asig_salario_in = models.IntegerField()
    asig_salario_out = models.CharField(max_length=150)
    asig_tipo_empleado = models.CharField(max_length=1)
    grup_clave = models.IntegerField()
    grup_nombre = models.CharField(max_length=240)
    grup_bandera_habilitado = models.CharField(max_length=1)
    grup_nomina_jde = models.CharField(max_length=60)
    grup_compania_jde = models.CharField(max_length=60)
    grup_proyecto_jde = models.CharField(max_length=60)
    grup_proyecto_code_jde = models.CharField(max_length=30)
    grup_fase_jde = models.CharField(max_length=60)
    grup_fase_code_jde = models.CharField(max_length=30)
    grup_puesto_jde = models.CharField(max_length=60)
    grup_puesto_code_jde = models.CharField(max_length=30)
    metodo_asignacion_id = models.IntegerField()
    metodo_nombre = models.CharField(max_length=80)
    metodo_tipo = models.CharField(max_length=80)
    metodo_prioridad = models.IntegerField()
    metodo_fecha_efec_desde = models.DateField()
    metodo_fecha_efec_hasta = models.DateField()
    metodo_importe_saldo = models.IntegerField()
    metodo_porcentaje = models.IntegerField()
    metodo_pago = models.CharField(max_length=150)
    metodo_sucursal = models.CharField(max_length=150)
    metodo_cuenta = models.CharField(max_length=150)
    metodo_banco = models.CharField(max_length=80)
    metodo_tipo_cuenta_id = models.CharField(max_length=150)
    metodo_clabe = models.CharField(max_length=150)

    def _get_nombre_foto(self):
        try:
            if self.pers_segundo_nombre == '-':
                nombre = '%s %s %s' % (self.pers_primer_nombre,
                                       self.pers_apellido_paterno,
                                       self.pers_apellido_materno)
                formato = nombre.replace(" ", "_")
                return formato
            else:
                nombre = '%s %s %s %s' % (self.pers_primer_nombre,
                                          self.pers_segundo_nombre,
                                          self.pers_apellido_paterno,
                                          self.pers_apellido_materno)
                formato = nombre.replace(" ", "_")
                return formato
        except Exception:
            return 0.0
    nombre_foto = property(_get_nombre_foto)

    class Meta:
        managed = False
        db_table = u'"NUVAPP"."VIEW_EMPLEADOS_FULL"'


class VIEW_TIPO_PERSONAS(models.Model):
    clave_tipo = models.IntegerField(primary_key=True)
    desc_tipo = models.CharField(max_length=80)

    class Meta:
        managed = False
        db_table = u'"NUVAPP"."VIEW_TIPO_PERSONAS"'


class VIEW_PUESTOS(models.Model):
    clave_puesto = models.IntegerField(primary_key=True)
    desc_puesto = models.CharField(max_length=240)

    class Meta:
        managed = False
        db_table = u'"NUVAPP"."VIEW_PUESTOS"'


class VIEW_ORGANIZACIONES(models.Model):
    clave_org = models.IntegerField(primary_key=True)
    desc_org = models.CharField(max_length=240)

    class Meta:
        managed = False
        db_table = u'"NUVAPP"."VIEW_ORGANIZACIONES"'


class VIEW_GRADO_ACADEMICO(models.Model):
    clave_grado = models.IntegerField(primary_key=True)
    desc_grado = models.CharField(max_length=240)

    class Meta:
        managed = False
        db_table = u'"NUVAPP"."VIEW_GRADO_ACADEMICO"'


class VIEW_ORGANIGRAMA(models.Model):

    pers_clave = models.IntegerField(primary_key=True)
    pers_empleado_numero = models.IntegerField()
    pers_nombre_completo = models.CharField(max_length=240)
    asig_trabajo_desc = models.CharField(max_length=240)
    asig_organizacion_desc = models.CharField(max_length=240)
    asig_puesto_desc = models.CharField(max_length=240)
    grup_compania_jde = models.CharField(max_length=240)
    grup_proyecto_jde = models.CharField(max_length=240)
    asig_jefe_directo_clave = models.CharField(max_length=240)
    jefe_nombre_completo = models.CharField(max_length=240)
    nivel_estructura = models.IntegerField()
    ruta = models.CharField(max_length=240)
    ruta2 = models.CharField(max_length=240)
    asig_organizacion_clave = models.IntegerField()
    grup_fase_jde = models.CharField(max_length=240)
    asig_ubicacion_desc = models.CharField(max_length=240)
    tipo = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = u'"NUVAPP"."VIEW_ORGANIGRAMA"'


class VIEW_ESPECIALIDADES(models.Model):

    qua_especialidad = models.CharField(primary_key=True, max_length=255)

    class Meta:
        managed = False
        db_table = u'"NUVAPP"."VIEW_ESPECIALIDADES"'


class VIEW_COMPETENCIAS(models.Model):

    competence_id = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=740)

    class Meta:
        managed = False
        db_table = u'"NUVAPP"."VIEW_COMPETENCIAS"'


class VIEW_COMPANIAS(models.Model):
    desc_compania = models.CharField(primary_key=True, max_length=60)

    class Meta:
        managed = False
        db_table = u'"NUVAPP"."VIEW_COMPANIAS"'
