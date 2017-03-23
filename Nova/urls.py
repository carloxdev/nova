
# Liberias Django
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include

# Librerias APi Rest:
from rest_framework import routers

# API Rest Vistas:
from finanzas.views import ViaticoCabeceraAPI
from finanzas.views import ViaticoLineaAPI


router = routers.DefaultRouter()

router.register(
    r'viaticocabecera',
    ViaticoCabeceraAPI,
    'viaticocabecera'
)

router.register(
    r'viaticolinea',
    ViaticoLineaAPI,
    'viaticolinea'
)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('finanzas.urls', namespace="finanzas")),
    url(r'', include('home.urls', namespace="home")),
    url(r'', include('seguridad.urls', namespace="seguridad")),

    url(r'^api/', include(router.urls)),
]
