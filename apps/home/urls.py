from django.urls import path, re_path
from apps.home import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    path('consultas_dni', views.consultas, name='consultas'),
    path('consultas_otras', views.otras_consultas, name='otras_consultas'),
    path('padron_activos', views.padron_activos, name='padron_activos'),
    path('padron_inactivos', views.padron_inactivos, name='padron_inactivos'),

    # Otras consultas
    path('grupo_familiar', views.grupo_familiar, name="grupo_familiar"),
    path('grupo_familiar/<int:dni>', views.grupo_familiar, name="grupo_familiar_detalle"),

    path('beneficiarios_envase', views.beneficiarios_envase, name='beneficiarios_envase'),
    path('beneficiarios_envase/<int:tipo>', views.beneficiarios_envase, name='beneficiarios_envase_detalle'),

    path('beneficiarios_barrio', views.beneficiarios_barrio, name='beneficiarios_barrio'),
    path('beneficiarios_barrio/<str:barrio>', views.beneficiarios_barrio, name='beneficiarios_barrio_detalle'),

    path('beneficiarios_localidad', views.beneficiarios_localidad, name='beneficiarios_localidad'),
    path('beneficiarios_localidad/<str:localidad>', views.beneficiarios_localidad, name='beneficiarios_localidad_detalle'),

    path('descargas_empresas', views.descargas_empresa, name='descargas_empresas'),
    path('cantidad_envases', views.cantidad_envases, name='cantidad_envases'),


    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),
]