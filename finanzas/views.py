# -*- coding: utf-8 -*-

# Django's Libraries
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.views.generic.base import View
from django.contrib import messages

# Own's Libraries
from .models import ViaticoCabecera

from .business import ViaticoBusiness

from .forms import ViaticoCabeceraForm
from .forms import ViaticoFilterForm
from .forms import ViaticoLineaForm

from .forms import AnticipoFilterForm

from home.utilities import get_Url_With_Querystring


class ViaticoLista(View):
    template_name = 'viatico/viatico_lista.html'

    def get(self, request):

        formulario = ViaticoFilterForm()

        contexto = {
            'form': formulario
        }

        return render(request, self.template_name, contexto)


class ViaticoCabeceraNuevo(View):
    template_name = 'viatico/viatico_nuevo.html'

    def get(self, request):

        formulario = ViaticoCabeceraForm()

        contexto = {
            'form': formulario
        }

        return render(request, self.template_name, contexto)

    def post(self, request):

        formulario = ViaticoCabeceraForm(request.POST)

        if formulario.is_valid():

            viatico_cabecera = formulario.save(commit=False)

            try:

                ViaticoBusiness.set_Data_Autorizacion(viatico_cabecera)
                ViaticoBusiness.set_Data_Compania(viatico_cabecera)

                viatico_cabecera.created_by = request.user.profile
                viatico_cabecera.updated_by = request.user.profile
                viatico_cabecera.save()

                return redirect(
                    get_Url_With_Querystring(
                        reverse('finanzas:viatico_editar', kwargs={'pk': viatico_cabecera.pk}),
                        new=True
                    )
                )

            except Exception as e:
                messages.error(request, str(e))

        contexto = {
            'form': formulario
        }
        return render(request, self.template_name, contexto)


class ViaticoCabeceraEditar(View):
    template_name = 'viatico/viatico_editar.html'

    def get(self, request, pk):

        if len(request.GET):
            flag_new = bool(request.GET['new'])
        else:
            flag_new = False

        formulario_cabecera = ViaticoCabeceraForm(
            instance=ViaticoBusiness.get_ViaticoCabevera(pk)
        )
        formulario_linea = ViaticoLineaForm()

        contexto = {
            'form_cabecera': formulario_cabecera,
            'form_linea': formulario_linea,
            'flag_new': flag_new
        }
        return render(request, self.template_name, contexto)

    def post(self, request, pk):

        formulario_cabecera = ViaticoCabeceraForm(
            request.POST,
            instance=ViaticoBusiness.get_ViaticoCabevera(pk)
        )
        formulario_linea = ViaticoLineaForm()

        if formulario_cabecera.is_valid():

            viatico_cabecera = formulario_cabecera.save(commit=False)

            try:
                ViaticoBusiness.set_Data_Autorizacion(viatico_cabecera)
                ViaticoBusiness.set_Data_Compania(viatico_cabecera)

                viatico_cabecera.updated_by = request.user.profile
                viatico_cabecera.save()
                messages.success(request, "Se modifico la solicitud exitosamente")

            except Exception as e:
                messages.error(request, str(e))

        contexto = {
            'form_cabecera': formulario_cabecera,
            'form_linea': formulario_linea
        }
        return render(request, self.template_name, contexto)


class AnticipoLista(View):
    def __init__(self):
        self.template_name = 'anticipo/anticipo_lista.html'

    def get(self, request):
        formulario = AnticipoFilterForm()

        contexto = {
            'form': formulario
        }

        return render(request, self.template_name, contexto)
