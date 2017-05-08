# -*- coding: utf-8 -*-
# Django:
from django.forms import TextInput
from django.forms import Select
from django.forms import Form

from django.forms import CharField
from django.forms import IntegerField
from django.forms import NumberInput
from django.forms import ChoiceField
from django.forms import RadioSelect

# Modelos
from jde.models import VIEW_COMPANIAS
from jde.models import VIEW_UNIDADES
from ebs.models import VIEW_TIPO_PERSONAS
from ebs.models import VIEW_PUESTOS
from ebs.models import VIEW_ORGANIZACIONES


class EmpleadosFilterForm(Form):
    GENERO = (
        ('F', 'Femenino'),
        ('M', 'Masculino'),
    )
    TIPO = (
        ('', '-------'),
        ('MHP', 'MHP'),
    )
    PUESTO = (
        ('', '-------'),
        ('A', 'Analista de medio ambiente'),
    )
    ORGANIZACION = (
        ('', '-------'),
        ('CV', 'Coordinacion Villahermosa'),
    )
    CENTRO_DE_COSTOS = (
        ('', '-------'),
        ('F201113', 'F201113'),
    )
    NOMINA = (
        ('ADMINISTRATIVA', 'Administrativa'),
        ('OPERATIVA', 'Operativa'),
    )

    pers_primer_nombre = CharField(widget=TextInput(attrs={'class': 'form-control input-xs'}))
    pers_segundo_nombre = CharField(widget=TextInput(attrs={'class': 'form-control input-xs'}))
    pers_apellido_paterno = CharField(widget=TextInput(attrs={'class': 'form-control input-xs'}))
    pers_apellido_materno = CharField(widget=TextInput(attrs={'class': 'form-control input-xs'}))
    pers_genero_clave = ChoiceField(widget=RadioSelect, choices=GENERO)
    pers_empleado_numero = IntegerField(widget=NumberInput(attrs={'class': 'form-control input-xs', 'min': '1'}))
    pers_tipo_codigo = ChoiceField(widget=Select(attrs={'class': 'select2 nova-select2'}), choices=TIPO)
    asig_puesto_clave = ChoiceField(widget=Select(attrs={'class': 'select2 nova-select2'}), choices=PUESTO)
    asig_organizacion_clave = ChoiceField(widget=Select(attrs={'class': 'select2 nova-select2'}), choices=ORGANIZACION)
    grup_compania_jde = ChoiceField(widget=Select(attrs={'class': 'select2 nova-select2'}), choices=ORGANIZACION)
    zona = CharField(widget=TextInput(attrs={'class': 'form-control input-xs'}))  # PREGUNTAR POR EL CAMPO
    metodo_sucursal = ChoiceField(widget=Select(attrs={'class': 'select2 nova-select2'}), choices=CENTRO_DE_COSTOS)
    grup_nomina_jde = ChoiceField(widget=RadioSelect, choices=NOMINA)

    def __init__(self, *args, **kwargs):
        super(EmpleadosFilterForm, self).__init__(
            *args, **kwargs)
        self.fields['pers_tipo_codigo'].choices = self.get_Tipos()
        self.fields['asig_puesto_clave'].choices = self.get_Puestos()
        self.fields['asig_organizacion_clave'].choices = self.get_Organizacion()
        self.fields['grup_compania_jde'].choices = self.get_Compania()
        self.fields['metodo_sucursal'].choices = self.get_Sucursal()

    def get_Tipos(self):

        valores = [('', '-------')]

        tipos = VIEW_TIPO_PERSONAS.objects.using('ebs_d').all()

        for tipo in tipos:

            valores.append(
                (
                    tipo.clave_tipo,
                    str(int(tipo.clave_tipo)) + ' - ' + tipo.desc_tipo,
                )
            )
        return valores

    def get_Puestos(self):

        valores = [('', '-------')]

        puestos = VIEW_PUESTOS.objects.using('ebs_d').all()

        for puesto in puestos:

            valores.append(
                (
                    puesto.clave_puesto,
                    str(int(puesto.clave_puesto)) + ' - ' + puesto.desc_puesto,
                )
            )
        return valores

    def get_Organizacion(self):

        valores = [('', '-------')]

        organizaciones = VIEW_ORGANIZACIONES.objects.using('ebs_d').all()

        for organizacion in organizaciones:

            valores.append(
                (
                    organizacion.clave_org,
                    str(int(organizacion.clave_org)) + ' - ' + organizacion.desc_org,
                )
            )
        return valores

    def get_Compania(self):

        valores = [('', '-------')]

        companias = VIEW_COMPANIAS.objects.using('jde_p').all()

        for compania in companias:

            valores.append(
                (
                    compania.comp_code,
                    str(int(compania.comp_code)) + ' - ' + compania.comp_desc,
                )
            )
        return valores

    def get_Sucursal(self):

        valores = [('', '-------')]

        unidades = VIEW_UNIDADES.objects.using('jde_p').all()

        for unidad in unidades:

            valores.append(
                (
                    unidad.clave,
                    '(' + unidad.clave + ')' + ' ' + unidad.desc_corta,
                )
            )
        return valores
