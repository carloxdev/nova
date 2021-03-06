
# Librerias APi Rest:
from rest_framework import routers

# API Rest Vistas:
from .views_rest import ViaticoCabeceraAPI
from .views_rest import ViaticoCabeceraByPageAPI
from .views_rest import ViaticoLineaAPI

router_viaticos = routers.DefaultRouter()

router_viaticos.register(
    r'viaticocabecera',
    ViaticoCabeceraAPI,
    'viaticocabecera'
)
router_viaticos.register(
    r'viaticocabecera_bypage',
    ViaticoCabeceraByPageAPI,
    'viaticocabecera_bypage'
)
router_viaticos.register(
    r'viaticolinea',
    ViaticoLineaAPI,
    'viaticolinea'
)
