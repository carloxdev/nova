# -*- coding: utf-8 -*-
# Django:
from django.forms import ModelForm
from django import forms

from django.forms import TextInput
from django.forms import FileInput
from django.forms import CharField
from django.forms import DateInput
from django.forms import Select
from django.forms import PasswordInput
from django.forms import ChoiceField

from .models import User
from .models import Profile
from ebs.models import VIEW_EMPLEADOS_SIMPLE


class UserFormFilter(forms.Form):
    usuario = CharField(label="Nombre de usuario:")
    usuario__first_name = CharField(label="Nombre:")
    usuario__last_name = CharField(label="Apellidos:")
    usuario__email = CharField(label="Email:")
    clave_rh = CharField(label="Clave RH:")
    usuario__date_joined_mayorque = CharField(label="Fecha de creación mayor a:")
    usuario__date_joined_menorque = CharField(label="Fecha de creación menor a:")


class UserForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['is_active'].initial = True

    class Meta:
        model = User

        fields = ['password',
                  'username',
                  'first_name',
                  'last_name',
                  'email',
                  'is_active',
                  'is_staff',
                  'last_login',
                  ]

        labels = {'password': 'Contraseña',
                  'username': 'Nombre de usuario',
                  'first_name': 'Nombre',
                  'last_name': 'Apellidos',
                  'email': 'Email',
                  'is_active': 'Activo',
                  'is_staff': 'Administrador',
                  'last_login': 'Ultima sesion',
                  }

        widgets = {'password': PasswordInput(attrs={'class': 'form-control input-xs'}),
                   'username': TextInput(attrs={'class': 'form-control input-xs'}),
                   'first_name': TextInput(attrs={'class': 'form-control input-xs'}),
                   'last_name': TextInput(attrs={'class': 'form-control input-xs'}),
                   'email': TextInput(attrs={'class': 'form-control input-xs'}),
                   }  #Para hacer no editable 'disabled': 'True'

class UsuarioForm(ModelForm):
    #clave_rh = ChoiceField(label="Clave de empleado:",widget = Select(attrs={'class': 'form-control input-xs'}))
        
    class Meta:
        model = Profile

        fields = ['clave_rh',
                  'clave_jde',
                  'fecha_nacimiento',
                  'foto',
                  ]

        labels = {'clave_rh': 'Clave de empleado',
                  'clave_jde': 'Clave jde',
                  'fecha_nacimiento': 'Fecha de nacimiento',
                  'foto': 'Foto',
                  }

        widgets = {
                   'clave_rh': TextInput(attrs={'class': 'form-control input-xs'}),
                   'clave_jde': TextInput(attrs={'class': 'form-control input-xs'}),
                   'fecha_nacimiento': DateInput(attrs={'class': 'form-control input-xs', 'data-date-format': 'yyyy-mm-dd'}),
                   'foto': FileInput(attrs={'class': 'dropzone dz-clickable dz-started'}),
                   }

    # def __init__(self, *args, **kwargs):
    #     super(UsuarioForm, self).__init__(*args, **kwargs)
    #     self.fields['clave_rh'].choices= self.get_Clave_rh()

    # def get_Clave_rh(self):

    #     valores = [('','-------')]

    #     claves = VIEW_EMPLEADOS_SIMPLE.objects.using('ebs_d').all()
        

    #     for clave in claves:

    #         valores.append(
    #             (   
    #                 clave.pers_empleado_numero,
    #                 clave.pers_empleado_numero,
    #             )
    #         )
    #     return valores


class UserEditarForm(ModelForm):

    # def __init__(self, *args, **kwargs):
    #     super(UserEditarForm, self).__init__(*args, **kwargs)
    #     self.fields['password'].required = False

    class Meta:
        model = User

        fields = [#'password',
                  'first_name',
                  'last_name',
                  'email',
                  'is_active',
                  'is_staff',
                  ]

        labels = {#'password': 'Contraseña',
                  'first_name': 'Nombre',
                  'last_name': 'Apellidos',
                  'email': 'Email',
                  'is_active': 'Activo',
                  'is_staff': 'Administrador'
                  }

        widgets = {#'password': PasswordInput(attrs={'class': 'form-control input-xs'}),
                   'first_name': TextInput(attrs={'class': 'form-control input-xs'}),
                   'last_name': TextInput(attrs={'class': 'form-control input-xs'}),
                   'email': TextInput(attrs={'class': 'form-control input-xs'}),
                   }

class UserEditarPerfilForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(UserEditarPerfilForm, self).__init__(*args, **kwargs)
        self.fields['password'].required = False

    class Meta:
        model = User

        fields = ['password',
                  'first_name',
                  'last_name',
                  'email',
                  ]

        labels = {'password': 'Contraseña',
                  'first_name': 'Nombre',
                  'last_name': 'Apellidos',
                  'email': 'Email',
                  }

        widgets = {'password': PasswordInput(attrs={'class': 'form-control input-xs'}),
                   'first_name': TextInput(attrs={'class': 'form-control input-xs'}),
                   'last_name': TextInput(attrs={'class': 'form-control input-xs'}),
                   'email': TextInput(attrs={'class': 'form-control input-xs'}),
                   }  

class UserContrasenaForm(forms.Form):

    # contrasena_actual = CharField(label="Actual",
    #                         widget=forms.PasswordInput(
    #                             attrs={'class': 'form-control input-xs'}))

    contrasena_nueva = CharField(label="Nueva",
                            widget=forms.PasswordInput(
                                attrs={'class': 'form-control input-xs'}))

class ConfirmarForm(forms.Form):
    confirmar = CharField(label="Confirmación:",
                          widget=forms.PasswordInput(
                              attrs={'class': 'form-control input-xs'})
                          )
