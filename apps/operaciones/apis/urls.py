from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from apps.operaciones.apis.api import *

app_name='api'

urlpatterns = [
    ## Operaciones mensuales
    path('operaciones_mensuales/mes_actual/<int:dni>/', operaciones_mes_actual_api_view , name='operaciones_mes_actual_api_view' ),
    path('operaciones_mensuales/mes_anterior/<int:dni>/', operaciones_mes_anterior_api_view , name='operaciones_mes_anterior_api_view' ),
    path('operaciones_mensuales/dos_meses_atras/<int:dni>/', operaciones_dos_meses_atras_api_view , name='operaciones_dos_meses_atras_api_view' ),
    path('operaciones_mensuales/consumo_extendido/<int:dni>/<str:desde>/<str:hasta>/', operaciones_dos_meses_atras_api_view , name='operaciones_dos_meses_atras_api_view' ),

    path('operaciones_mensuales/asignacion/<int:dni>/', asignacion_por_dni_api_view , name='asignacion_por_dni_api_view' ),
    path('operaciones_mensuales/descarga/<int:dni>/', descargas_por_dni_api_view , name='descargas_por_dni_api_view' ),
    path('operaciones_mensuales/saldo/<int:dni>/', saldos_api_view , name='saldos_api_view' ),

    ## Padrones
    path('padron_beneficiarios/', padron_beneficiarios_api_view , name='padron_beneficiarios_api_view' ),
    path('padron_sin_consumo/', padron_sin_consumo_api_view , name='padron_sin_consumo_api_view' ),
    path('padron_sin_consumo/<str:desde>/', padron_sin_consumo_api_view , name='padron_sin_consumo_api_view' ),

    ## Otras consultas
    path('grupo_familiar/', grupo_familiar_api_view, name='grupo_familiar_api_view' ),
    path('grupo_familiar/<int:dni>/', grupo_familiar_api_view, name='grupo_familiar_api_view' ),

    path('beneficiario/<int:dni>/', beneficiario_api_view , name='beneficiario_api_view' ),

    path('beneficiarios_por_envase/', beneficiarios_por_envase_api_view, name='beneficiarios_por_envase_api_view' ),
    path('beneficiarios_por_envase/<int:tipo>/', beneficiarios_por_envase_api_view, name='beneficiarios_por_envase_api_view' ),

    path('beneficiarios_por_barrio/', beneficiarios_por_barrio_api_view, name='beneficiarios_por_barrio_api_view' ),
    path('beneficiarios_por_barrio/<str:barrio>/', beneficiarios_por_barrio_api_view, name='beneficiarios_por_barrio_api_view' ),

    path('beneficiarios_por_localidad/', beneficiarios_por_localidad_api_view, name='beneficiarios_por_localidad_api_view' ),
    path('beneficiarios_por_localidad/<str:localidad>/', beneficiarios_por_localidad_api_view, name='beneficiarios_por_localidad_api_view' ),

    path('cantidad_envases/', cantidad_envases_api_view, name='cantidad_envases_api_view' ),
    path('descargas_por_empresa/', descargas_por_empresa_api_view, name='descargas_por_empresa_api_view' ),

    path('auth/', obtain_auth_token, name='auth'),
]
