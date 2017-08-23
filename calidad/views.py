# -*- coding: utf-8 -*-

# Librerias/Clases Python
import datetime

# Librerias/Clases Django
from django.shortcuts import render
from django.views.generic.base import View
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.core.urlresolvers import reverse_lazy

# Django Urls:
from django.core.urlresolvers import reverse

# Django Urls:
from django.http import HttpResponse

# Librerias/Clases de Terceros

# Librerias/Clases propias

# Modelos:
from .models import Criterio
from .models import Proceso
from .models import Rol
from .models import Formato
from .models import Auditoria
from administracion.models import Contrato
from jde.models import VIEW_CONTRATO
from .models import Criterio
from .models import AuditoriaContrato
from .models import CompaniaAccion

# Otros Modelos:


# Formularios:
from .forms import CriterioForm
from .forms import RequisitoFilterForm
from .forms import RequisitoForm
from .forms import ProcesoForm
from .forms import SubprocesoForm
from .forms import ResponsableForm
from .forms import RolForm
from .forms import RolFilterForm
from .forms import CompaniaRolForm
from .forms import SitioForm
from .forms import MetodologiaForm
from .forms import FallaForm
from .forms import FormatoForm
from .forms import GeneralAuditoriaForm
from .forms import AuditorForm
from .forms import AuditoriaProcesoForm

# Serializadore:
from .serializers import RequisitoSerilizado
from .serializers import SubprocesoSerilizado


# ----------------- CALIDAD - Dashboard ----------------- #


class CalidadDashboard(View):

    def __init__(self):
        self.template_name = 'dashboard/calidad_dashboard.html'

    def get(self, request):

        # formulario = EmpleadoFilterForm()

        # contexto = {
        #     'form': formulario
        # }

        return render(request, self.template_name, {})


# ----------------- CALIDAD - AUDITORIAS ----------------- #

class AuditoriaLista(View):

    def __init__(self):
        self.template_name = 'auditoria/auditoria_lista.html'

    def get(self, request):

        auditorias = Auditoria.objects.all()
        # formulario = EmpleadoFilterForm()

        contexto = {
            # 'form': formulario
            'auditorias' : auditorias
        }

        return render(request, self.template_name, contexto)


class GeneralFormularioCreate(View):

    def __init__(self):
        self.template_name = 'auditoria/general_formulario.html'

    def get(self, request):

        formulario = GeneralAuditoriaForm()

        contexto = {
            'form': formulario,
            'operation': 'Nuevo'
        }

        return render(request, self.template_name, contexto)

    def post(self, request):

        formulario = GeneralAuditoriaForm(request.POST)

        if formulario.is_valid():
            datos_formulario = formulario.cleaned_data
            auditoria = Auditoria()
            compania = datos_formulario.get('compania')
            autorizador = Rol.objects.filter(companiaaccion__compania_codigo=compania.split(':')[0], rol='Autorizador' )
            aprobador = Rol.objects.filter(companiaaccion__compania_codigo=compania.split(':')[0], rol='Aprobador' )
            auditoria.folio = self.get_Folio()
            auditoria.tipo_auditoria = datos_formulario.get('tipo_de_auditoria')
            auditoria.compania = compania
            if datos_formulario.get('fecha_programada_ini') is not u'':
                auditoria.fecha_programada_inicial = datos_formulario.get('fecha_programada_ini')
            if datos_formulario.get('fecha_programada_fin') is not u'':
                auditoria.fecha_programada_final = datos_formulario.get('fecha_programada_fin')
            auditoria.objetivo = datos_formulario.get('objetivo')
            auditoria.alcance = datos_formulario.get('alcance')
            auditoria.recurso_necesario = datos_formulario.get('recursos_necesarios')
            auditoria.estado = 'En Captura'
            auditoria.autorizador = autorizador[0].nombre_completo
            auditoria.aprobador = aprobador[0].nombre_completo
            auditoria.save()

            for criterio in datos_formulario.get('criterios'):
                cri = Criterio.objects.get(pk=criterio)
                auditoria.criterio.add(cri)

            for contrato in datos_formulario.get('contratos'):
                contratos = AuditoriaContrato()
                contratos.id_auditoria = Auditoria.objects.get(pk =  auditoria.pk)
                contratos.id_contrato = contrato
                contratos.save()

            return redirect(reverse('calidad:auditor_formulario_update', kwargs={'pk': auditoria.pk}))

        contexto = {
            'form': formulario,
            'operation': 'Nuevo',
            'pk': auditoria.pk
        }

        return render(request, self.template_name, contexto)

    def get_Folio(self):
        fecha = datetime.datetime.now()
        last_digits = str(fecha.year)[2:]
        auditorias = Auditoria.objects.filter(folio__icontains=last_digits)
        noAuditoria = ""
        no_aud_act = 1

        if len(auditorias):
            for auditoria in auditorias:
                folio = int(auditoria.folio.split("-")[1])
                if folio > no_aud_act:
                    no_aud_act = folio
            no_aud_act = no_aud_act + 1

        if len(str(no_aud_act)) == 1:
            noAuditoria = "0"+str(no_aud_act)
        return "AUD-" +noAuditoria+ "-" + last_digits


class GeneralFormularioUpdate(View):

    def __init__(self):
        self.template_name = 'auditoria/general_formulario.html'

    def get(self, request, pk):

        auditoria = get_object_or_404( Auditoria, pk=pk )
        contratos = []
        criterios = []

        for contrato in AuditoriaContrato.objects.filter( id_auditoria=pk ):
            contratos.append(contrato.id_contrato)

        for criterio in auditoria.criterio.all():
            criterios.append(criterio.pk)

        initial_data = {
            'tipo_de_auditoria' : auditoria.tipo_auditoria,
            'compania' : auditoria.compania,
            'contratos' : contratos,
            'criterios' : criterios,
            'fecha_programada_ini': auditoria.fecha_programada_inicial,
            'fecha_programada_fin': auditoria.fecha_programada_final,
            'objetivo': auditoria.objetivo,
            'alcance': auditoria.alcance,
            'recursos_necesarios': auditoria.recurso_necesario,
        }

        formulario = GeneralAuditoriaForm( initial=initial_data )

        contexto = {
            'form': formulario,
            'operation': 'Editar',
            'folio': auditoria.folio,
            'pk': pk,
        }

        return render(request, self.template_name, contexto)

    def post(self, request, pk):

        formulario = GeneralAuditoriaForm( request.POST )
        auditoria = get_object_or_404( Auditoria, pk=pk )

        if formulario.is_valid():
            datos_formulario = formulario.cleaned_data

            contrato = VIEW_CONTRATO()
            criterio = Criterio()
            auditoria.tipo_auditoria = datos_formulario.get('tipo_de_auditoria')
            auditoria.compania = datos_formulario.get('compania')
            if datos_formulario.get('fecha_programada_ini') is not u'':
                auditoria.fecha_programada_inicial = datos_formulario.get('fecha_programada_ini')
            if datos_formulario.get('fecha_programada_fin') is not u'':
                auditoria.fecha_programada_final = datos_formulario.get('fecha_programada_fin')
            auditoria.objetivo = datos_formulario.get('objetivo')
            auditoria.alcance = datos_formulario.get('alcance')
            auditoria.recurso_necesario = datos_formulario.get('recursos_necesarios')
            auditoria.save()

            aud_cri_list_db = []
            aud_con_list_db = []

            for criterio_lista in auditoria.criterio.all():
                aud_cri_list_db.append(criterio_lista.id)

            for criterio in datos_formulario.get('criterios'):
                cri = Criterio.objects.get(pk=criterio)

                if cri.pk in aud_cri_list_db:
                    aud_cri_list_db.remove(cri.pk)
                else:
                    auditoria.criterio.add(cri)

            for lista in aud_cri_list_db:
                auditoria.criterio.remove(Criterio.objects.get(pk=lista))

            contratos = AuditoriaContrato.objects.filter(id_auditoria = pk)

            for contrato in contratos:
                aud_con_list_db.append(contrato.id_contrato)

            for contrato in datos_formulario.get('contratos'):

                if contrato in aud_con_list_db:

                    aud_con_list_db.remove(contrato)
                else:
                    con = AuditoriaContrato()
                    con.id_contrato = contrato
                    con.id_auditoria = Auditoria.objects.get(pk =  auditoria.pk)
                    con.save()

            for lista in aud_con_list_db:
                AuditoriaContrato.objects.filter(id_auditoria = auditoria.pk, id_contrato = lista).delete()

            return redirect(reverse('calidad:general_formulario_update', kwargs={'pk': auditoria.pk}))

        contratos = []
        criterios = []

        for contrato in AuditoriaContrato.objects.filter( id_auditoria=pk ):
            contratos.append(contrato.id_contrato)

        for criterio in auditoria.criterio.all():
            criterios.append(criterio.pk)

        initial_data = {
            'tipo_de_auditoria' : auditoria.tipo_auditoria,
            'compania' : auditoria.compania,
            'contratos' : contratos,
            'criterios' : criterios,
            'fecha_programada_ini': auditoria.fecha_programada_inicial,
            'fecha_programada_fin': auditoria.fecha_programada_final,
            'objetivo': auditoria.objetivo,
            'alcance': auditoria.alcance,
            'recursos_necesarios': auditoria.recurso_necesario,
        }

        formulario = GeneralAuditoriaForm( initial=initial_data )

        contexto = {
            'form': formulario,
            'operation': 'Editar',
            'folio': auditoria.folio,
            'pk': pk,
        }

        return render(request, self.template_name, contexto)


class AuditorFormularioUpdate(View):

    def __init__(self):
        self.template_name = 'auditor/auditor_formulario.html'

    def get(self, request, pk):
        auditoria = get_object_or_404( Auditoria, pk = pk )
        compania_codigo = auditoria.compania.split(':')[0]
        auditor_lider = Rol.objects.filter(companiaaccion__compania_codigo=compania_codigo, rol='Auditor Lider' )


        auditores_designados = []
        auditores_colaboradores = []

        for aud_des in auditoria.auditores_designados.all():
            auditores_designados.append(aud_des.pk)

        for aud_col in auditoria.auditores_colaboradores.all():
            auditores_colaboradores.append(aud_col.pk)

        initial_data = {
            'auditor_lider': auditor_lider[0].nombre_completo,
            'auditores_designados': auditores_designados,
            'auditores_colaboradores': auditores_colaboradores
        }

        formulario = AuditorForm( initial = initial_data )

        contexto = {
            'form': formulario,
            'folio': auditoria.folio,
            'pk': auditoria.pk,
            'operation': 'Editar',
        }

        return render(request, self.template_name, contexto)

    def post(self, request, pk):
        formulario = AuditorForm(request.POST)
        auditoria = Auditoria.objects.get(pk = pk)

        if formulario.is_valid():
            datos_formulario = formulario.cleaned_data

            rol = Rol()
            auditoria.auditor_lider = datos_formulario.get('auditor_lider')
            auditoria.save()
            for auditores_designados in datos_formulario.get('auditores_designados'):
                aud_des = Rol.objects.get(pk=auditores_designados)
                auditoria.auditores_designados.add(aud_des)

            for auditores_colaboradores in datos_formulario.get('auditores_colaboradores'):
                aud_col = Rol.objects.get(pk=auditores_colaboradores)
                auditoria.auditores_colaboradores.add(aud_col)

            return redirect(reverse('calidad:proceso_lista', kwargs={'pk': auditoria.pk}))

        contexto = {
            'form': formulario,
            'folio': auditoria.folio,
            'pk': auditoria.pk,
            'operation': 'Editar',
        }

        return render(request, self.template_name, contexto)


class ProcesoLista(View):

    def __init__(self):
        self.template_name = 'proceso/proceso_lista.html'

    def get(self, request, pk):

        auditoria = get_object_or_404(Auditoria, pk = pk)
        auditores_designados = self.get_AuditoresDesignados( auditoria )

        formulario = AuditoriaProcesoForm( auditores_designados )

        contexto = {
            'pk': pk,
            'form': formulario
        }

        return render(request, self.template_name, contexto)

    def get_AuditoresDesignados(self, auditoria):

        valores = [('', '-------')]

        for aud_des in auditoria.auditores_designados.all():

            valores.append(
                (
                    aud_des.pk,
                    aud_des.numero_empleado + ' : ' + aud_des.nombre_completo
                )
            )
        return valores


class ProcesoFormulario(View):

    def __init__(self):
        self.template_name = 'proceso/proceso_formulario.html'

    def get(self, request, pk):

        # formulario = EmpleadoFilterForm()

        contexto = {
            # 'form': formulario
            'pk': pk
        }

        return render(request, self.template_name, contexto)


class RequisitoLista(View):

    def __init__(self):
        self.template_name = 'requisito_auditoria/requisito_lista.html'

    def get(self, request):

        # formulario = EmpleadoFilterForm()

        # contexto = {
        #     'form': formulario
        # }

        return render(request, self.template_name, {})


class HallazgoLista(View):

    def __init__(self):
        self.template_name = 'hallazgo/hallazgo_lista.html'

    def get(self, request):

        # formulario = EmpleadoFilterForm()

        # contexto = {
        #     'form': formulario
        # }

        return render(request, self.template_name, {})


class HallazgoDetalle(View):

    def __init__(self):
        self.template_name = 'hallazgo/hallazgo_detalle.html'

    def get(self, request):

        # formulario = EmpleadoFilterForm()

        # contexto = {
        #     'form': formulario
        # }

        return render(request, self.template_name, {})


# class EvidenciaFormulario(View):
#     def __init__(self):
#         self.template_name = 'evidencia/evidencia_formulario.html'

#     def get(self, request):

#         # formulario = EmpleadoFilterForm()

#         # contexto = {
#         #     'form': formulario
#         # }

#         return render(request, self.template_name, {})


# class PlanAccionLista(View):
#     def __init__(self):
#         self.template_name = 'plan_accion/plan_accion_lista.html'

#     def get(self, request):

#         # formulario = EmpleadoFilterForm()

#         # contexto = {
#         #     'form': formulario
#         # }

#         return render(request, self.template_name, {})


# class SeguimientoPlanAccionFormulario(View):
#     def __init__(self):
#         self.template_name = 'seguimiento_plan_accion/seguimiento_plan_accion_formulario.html'

#     def get(self, request):

#         # formulario = EmpleadoFilterForm()

#         # contexto = {
#         #     'form': formulario
#         # }

#         return render(request, self.template_name, {})


# ----------------- CALIDAD - PROGRAMA ----------------- #


class ProgramaLista(View):

    def __init__(self):
        self.template_name = 'programa_lista.html'

    def get(self, request):

        # formulario = EmpleadoFilterForm()

        # contexto = {
        #     'form': formulario
        # }

        return render(request, self.template_name, {})

# ----------------- CALIDAD - CONFIGURACION ----------------- #


class ConfiguracionCriterioLista(View):

    def __init__(self):
        self.template_name = 'criterio/configuracion_lista.html'

    def get(self, request):

        formularioCriterio = CriterioForm()
        formularioRequisito = RequisitoForm()
        formularioFiltro = RequisitoFilterForm()

        contexto = {
            'formularioCriterio': formularioCriterio,
            'formularioRequisito': formularioRequisito,
            'formularioFiltro': formularioFiltro
        }

        return render(request, self.template_name, contexto)


class ConfiguracionRequisitoAPI(View):

    def get(self, request):

        daddies = Criterio.objects.all()

        serializador = RequisitoSerilizado()
        lista_json = serializador.get_Json(daddies)
        return HttpResponse(
            lista_json,
            content_type="application/json"
        )


class ConfiguracionProcesoLista(View):

    def __init__(self):
        self.template_name = 'proceso/configuracion_lista.html'

    def get(self, request):

        formularioProceso = ProcesoForm()
        formularioSubproceso = SubprocesoForm()
        formularioResponsable = ResponsableForm()

        contexto = {
            'formularioProceso': formularioProceso,
            'formularioSubproceso': formularioSubproceso,
            'formularioResponsable': formularioResponsable
        }

        return render(request, self.template_name, contexto)


class ConfiguracionSubprocesoAPI(View):

    def get(self, request):

        daddies = Proceso.objects.all()

        serializador = SubprocesoSerilizado()
        lista_json = serializador.get_Json(daddies)
        return HttpResponse(
            lista_json,
            content_type="application/json"
        )


class ConfiguracionRolLista(View):

    def __init__(self):
        self.template_name = 'rol/configuracion_lista.html'

    def get(self, request):

        formularioRol = RolForm()
        formularioRolFiltro = RolFilterForm()
        formularioCompaniaRol = CompaniaRolForm()
        roles = Rol.objects.all()
        contexto = {
            'formularioRol': formularioRol,
            'formularioRolFiltro': formularioRolFiltro,
            'formularioCompaniaRol': formularioCompaniaRol,
            'roles': roles,
        }

        return render(request, self.template_name, contexto)

    # def post(self, request):

    #     formulario = RolForm(request.POST)

    #     if formulario.is_valid():
    #         datos_formulario = formulario.cleaned_data
    #         rol = Rol()
    #         texto = datos_formulario.get('empleado')
    #         datos = texto.split(":")
    #         numero_empleado = datos[0]
    #         nombre_completo = datos[1]
    #         rol.numero_empleado = numero_empleado
    #         rol.nombre_completo = nombre_completo
    #         rol.rol = datos_formulario.get('rol')
    #         rol.save()

    #         return redirect(reverse('calidad:configuracion_rol_lista'))

    #     contexto = {
    #         'form': formulario,
    #         'operation': 'Nuevo',
    #     }

    #     return render(request, self.template_name, contexto)


# class ConfiguracionRolNuevo(View):

#     def __init__(self):
#         self.template_name = 'rol/configuracion_lista.html'

#     def get(self, request):

#         formularioRol = RolForm()
#         formularioRolFiltro = RolFilterForm()
#         formularioCompaniaRol = CompaniaRolForm()
#         roles = Rol.objects.all()
#         contexto = {
#             'formularioRol': formularioRol,
#             'formularioRolFiltro': formularioRolFiltro,
#             'formularioCompaniaRol': formularioCompaniaRol,
#             'roles': roles,
#         }
#         return render(request, self.template_name, contexto)

#     def post(self, request):
#         formulario = RolForm(request.POST)

#         if formulario.is_valid():
#             datos_formulario = formulario.cleaned_data
#             rol = Rol()
#             texto = datos_formulario.get('empleado')
#             datos = texto.split(":")
#             numero_empleado = datos[0]
#             nombre_completo = datos[1]
#             rol.numero_empleado = numero_empleado
#             rol.nombre_completo = nombre_completo
#             rol.rol = datos_formulario.get('rol')
#             rol.save()

#             return redirect(reverse('calidad:configuracion_rol_lista'))

#         contexto = {
#             'form': formulario,
#             'operation': 'Nuevo',
#         }

#         return render(request, self.template_name, contexto)


# class ConfiguracionRolEditar(View):

#     def __init__(self):
#         self.template_name = 'rol/configuracion_lista.html'

#     def get(self, request):

#         formularioRol = RolForm()
#         formularioRolFiltro = RolFilterForm()
#         formularioCompaniaRol = CompaniaRolForm()
#         roles = Rol.objects.all()
#         contexto = {
#             'formularioRol': formularioRol,
#             'formularioRolFiltro': formularioRolFiltro,
#             'formularioCompaniaRol': formularioCompaniaRol,
#             'roles': roles,
#         }

#         return render(request, self.template_name, contexto)

#     def post(self, request):

#         rol = get_object_or_404(Rol, pk=pk)

#         formulario = RolForm(request.POST)

#         if formulario.is_valid():
#             datos_formulario = formulario.cleaned_data
#             rol = Rol()
#             texto = datos_formulario.get('empleado')
#             datos = texto.split(":")
#             numero_empleado = datos[0]
#             nombre_completo = datos[1]
#             rol.numero_empleado = numero_empleado
#             rol.nombre_completo = nombre_completo
#             rol.rol = datos_formulario.get('rol')
#             rol.save()

#             return redirect(reverse('calidad:configuracion_rol_lista'))

#         contexto = {
#             'form': formulario,
#             'operation': 'Nuevo',
#         }

#         return render(request, self.template_name, contexto)


class ConfiguracionSitioLista(View):

    def __init__(self):
        self.template_name = 'sitio/configuracion_lista.html'

    def get(self, request):

        formulario = SitioForm()

        contexto = {
            'form': formulario
        }

        return render(request, self.template_name, contexto)


class ConfiguracionMetodologiaLista(View):

    def __init__(self):
        self.template_name = 'metodologia/configuracion_lista.html'

    def get(self, request):

        formulario = MetodologiaForm()

        contexto = {
            'form': formulario
        }

        return render(request, self.template_name, contexto)


class ConfiguracionTipoFallaLista(View):

    def __init__(self):
        self.template_name = 'falla/configuracion_lista.html'

    def get(self, request):

        formulario = FallaForm()

        contexto = {
            'form': formulario
        }

        return render(request, self.template_name, contexto)


class ConfiguracionFormatoLista(View):

    def __init__(self):
        self.template_name = 'formato/configuracion_lista.html'

    def get(self, request):

        formulario = FormatoForm()
        formatos = Formato.objects.all()

        contexto = {
            'form': formulario,
            'formatos': formatos
        }

        return render(request, self.template_name, contexto)
