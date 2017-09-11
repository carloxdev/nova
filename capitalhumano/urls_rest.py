# Librerias APi Rest:
from rest_framework import routers

from .view_rest import PersonalAPI
from .view_rest import PersonalByPageAPI
from .view_rest import CapacitacionAPI
from .view_rest import CapacitacionByPageAPI
from capitalhumano.view_rest import DocumentoPersonalAPI
from capitalhumano.view_rest import DocumentoCapacitacionAPI
from capitalhumano.view_rest import ArchivoAPI
from capitalhumano.view_rest import PerfilPuestosCargoAPI
from capitalhumano.view_rest import PerfilPuestosCargoByPageAPI
from capitalhumano.view_rest import PerfilPuestosDocumentoAPI
from capitalhumano.view_rest import PerfilPuestosDocumentoByPageAPI
from capitalhumano.view_rest import PerfilCompetenciasAPI
from capitalhumano.view_rest import PerfilCompetenciasByPageAPI


router_capitalhumano = routers.DefaultRouter()

# --------------------DOCUMENTOS--------------------
router_capitalhumano.register(
    r'personal',
    PersonalAPI,
    'personal'
)
router_capitalhumano.register(
    r'personal_bypage',
    PersonalByPageAPI,
    'personal_bypage'
)
router_capitalhumano.register(
    r'capacitacion',
    CapacitacionAPI,
    'capacitacion'
)
router_capitalhumano.register(
    r'capacitacion_bypage',
    CapacitacionByPageAPI,
    'capacitacion_bypage'
)
router_capitalhumano.register(
    r'documentopersonal',
    DocumentoPersonalAPI,
    'documentopersonal'
)
router_capitalhumano.register(
    r'documentocapacitacion',
    DocumentoCapacitacionAPI,
    'documentocapacitacion'
)
router_capitalhumano.register(
    r'archivo',
    ArchivoAPI,
    'archivo'
)
# --------------------PERFILES--------------------
router_capitalhumano.register(
    r'perfilpuestoacargo_bypage',
    PerfilPuestosCargoByPageAPI,
    'perfilpuestoacargo_bypage'
)
router_capitalhumano.register(
    r'perfilpuestoacargo',
    PerfilPuestosCargoAPI,
    'perfilpuestosacargo'
)
router_capitalhumano.register(
    r'perfilpuestosdocumento',
    PerfilPuestosDocumentoAPI,
    'perfilpuestosdocumento'
)
router_capitalhumano.register(
    r'perfilpuestosdoc_bypage',
    PerfilPuestosDocumentoByPageAPI,
    'perfilpuestosdoc_bypage'
)

router_capitalhumano.register(
    r'perfilcompetencias',
    PerfilCompetenciasAPI,
    'perfilcompetencias'
)

router_capitalhumano.register(
    r'perfilcompetencias_bypage',
    PerfilCompetenciasByPageAPI,
    'perfilcompetencias_bypage'
)
