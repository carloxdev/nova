from django.conf.urls import url

# VISTAS
from .views import EmpleadoLista
from .views import EmpleadoDashboard
from .views import EmpleadoOrganigrama
from .views import PerfilPuesto
from .views import PerfilPuestoNuevo
from .views import PerfilPuestoNuevo2
from .views import PerfilPuestoConfiguraciones


urlpatterns = [
    url(r'^dashboard/$', EmpleadoDashboard.as_view(), name="empleado_dashboard"),
    url(r'^organigrama/$', EmpleadoOrganigrama.as_view(), name="empleado_organigrama"),
    url(r'^empleados/$', EmpleadoLista.as_view(), name="empleado_lista"),
    url(r'^perfilpuesto/$', PerfilPuesto.as_view(), name="perfil_lista"),
    url(r'^perfilpuesto/nuevo/$', PerfilPuestoNuevo.as_view(), name="perfil_nuevo"),
    url(r'^perfilpuesto/nuevo2/$', PerfilPuestoNuevo2.as_view(), name="perfil_nuevo2"),
    url(r'^perfilpuesto/configuraciones/$', PerfilPuestoConfiguraciones.as_view(), name="perfil_configuracion"),
]
