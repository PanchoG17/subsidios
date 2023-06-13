from django import template
from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse, HttpResponseRedirect
from django.core.exceptions import PermissionDenied
from django.template import loader
from django.urls import reverse

from core.services import *

## Method decorator
def is_agente(user, exc = True):
    if user.groups.filter(name='Agentes').exists():
        return True
    else:
        if exc:
            raise PermissionDenied()
        return False

## 403 Handler
def permission_denied(request, exception):
    context = {}
    return render(request, 'home/page-403.html', context, status=403)

@login_required(login_url="/login/")
def index(request):
    if request.user.groups.filter(name='Beneficiarios'):
        asignaciones = asignacion(request.user.username,request.user)
        descargas = descarga(request.user.username,request.user)
        saldos = saldo(request.user.username,request.user)

        # DESCARGAS MES ACTUAL
        if descargas:
            total_descargas=0
            for d in descargas or None:
                total_descargas += d['cantidad']
        else:
            total_descargas=None

        # ASIGNACION MES ACTUAL
        total = 0
        for a in asignaciones:
            total += a['cantidad']

        # OPERACIONES
        actual = mes_actual(request.user.username,request.user)
        anterior = mes_anterior(request.user.username,request.user)

        context = {'asignacion':total,'descargas':total_descargas,'saldo':saldos, 'asignaciones':asignaciones, 'anterior':anterior, 'actual':actual}
        return render(request, 'home/index_beneficiario.html',context)
    else:
        ## INACTIVOS
        inactivos = len(padron_sin_consumo(request.user))

        ## ACTIVOS POR LOCALIDADES
        activos = get_beneficiarios_por_localidad(request.user)
        total = 0
        for a in activos:
            total += a['localidad']

        ## CANTIDAD ASIGNACIONES POR ENVASE
        envases = get_cantidad_envases(request.user)

        context = {'segment': 'index', 'activos':activos,'inactivos':inactivos, 'total':total, 'envases':envases}
        return render(request, 'home/index_agente.html', context)

@user_passes_test(is_agente)
@login_required(login_url="/login/")
def padron_activos(request):
    padron = padron_beneficiarios(request.user)
    return render(request, 'home/padron.html', {'padron': padron, 'title':'Padrón activos'})

@user_passes_test(is_agente)
@login_required(login_url="/login/")
def padron_inactivos(request):
    desde = request.POST.get('desde')
    padron = padron_sin_consumo(request.user, desde) if desde else padron_sin_consumo(request.user)
    return render(request, 'home/padron.html', {'padron': padron,'title':'Padrón activos sin descargas'})

@login_required(login_url="/login/")
def consumo_dos_meses_anteriores(request):
    documento = request.POST.get('documento')
    data = dos_meses_anteriores(documento,request.user)
    title = 'Consumo últimos dos meses'

    context = { 'data': data, 'documento':documento, 'title': title}
    return render(request, 'home/consumos.html', context)

@login_required(login_url="/login/")
def consumo_periodo_extendido(request):
    documento = request.POST.get('documento')
    desde = request.POST.get('desde')
    hasta = request.POST.get('hasta')

    data = consumo_extendido(documento,request.user,desde,hasta)
    title = 'Consumo extendido'

    context = { 'data': data, 'documento':documento, 'title': title}
    return render(request, 'home/consumos.html', context)

@login_required(login_url="/login/")
def consumo_mes_anterior(request):
    documento = request.POST.get('documento')
    data = mes_anterior(documento,request.user)
    context = { 'data': data, 'documento':documento, 'title':'Consumo último mes' }
    return render(request, 'home/consumos.html', context)

@login_required(login_url="/login/")
def consumo_mes_actual(request):
    documento = request.POST.get('documento')
    data = mes_actual(documento,request.user)
    context = { 'data': data, 'documento':documento, 'title':'Consumo mes actual' }
    return render(request, 'home/consumos.html', context)

@login_required(login_url="/login/")
def saldo_actual(request):
    documento = request.POST.get('documento')
    saldos = saldo(documento,request.user)
    context = { 'saldos': saldos, 'documento':documento, 'title':'Saldo actual' }
    return render(request, 'home/saldos.html', context)

@login_required(login_url="/login/")
def descargas(request):
    documento = request.POST.get('documento')
    descargas = descarga(documento,request.user)
    context = { 'descargas': descargas, 'documento':documento, 'title':'Descargas' }
    return render(request, 'home/descargas.html', context)

@login_required(login_url="/login/")
def asignaciones(request):
    documento = request.POST.get('documento')
    data = asignacion(documento,request.user)
    context = { 'data': data, 'documento':documento, 'title':'Asignaciones' }
    return render(request, 'home/consumos.html', context)

@login_required(login_url="/login/")
def consultas(request):
    agente = is_agente(request.user, exc=False)
    if request.method == 'POST':

        if not agente and request.POST.get('documento') != request.user.username:
            raise PermissionDenied()

        if '0' in request.POST:
            response = consumo_mes_actual(request)
        if '1' in request.POST:
            response = consumo_mes_anterior(request)
        if '2' in request.POST:
            response = consumo_dos_meses_anteriores(request)
        if '3' in request.POST:
            response = asignaciones(request)
        if '4' in request.POST:
            response = descargas(request)
        if '5' in request.POST:
            response = saldo_actual(request)
        if 'desde' in request.POST:
            response = consumo_periodo_extendido(request)

    else:
        if agente:
            context = {'agente':agente,'documento':request.GET.get('documento'), 'title':'Consultar por DNI'}
            response = render(request, 'home/consultas.html',context)
        else:
            context = {'agente':agente,'documento':request.user.username, 'title':'Consulte sus movimientos'}
            response = render(request, 'home/consultas.html',context)
    return response


### Otras consultas agentes
def beneficiarios_envase(request, tipo = None):
    data = get_beneficiarios_por_envase(request.user,tipo) if tipo else get_beneficiarios_por_envase(request.user)
    envase = getEnvase(tipo) if tipo else None
    url = 'beneficiarios_envase'
    context = { 'padron': data, 'title':'Beneficiarios por envase asignado', 'envase':envase, 'detalle':envase, 'url':url}
    template = 'home/padron.html' if tipo else 'home/envases.html'
    return render(request, template, context)

def beneficiarios_barrio(request, barrio = None):
    data = get_beneficiarios_por_barrio(request.user,barrio) if barrio else get_beneficiarios_por_barrio(request.user)
    url = 'beneficiarios_barrio'
    context = { 'padron': data, 'title':'Beneficiarios por barrio','detalle':barrio, 'url':url}
    template = 'home/padron.html' if barrio else 'home/barrios.html'
    return render(request, template, context)

def beneficiarios_localidad(request, localidad = None):
    data = get_beneficiarios_por_localidad(request.user,localidad) if localidad else get_beneficiarios_por_localidad(request.user)
    url = 'beneficiarios_localidad'
    context = { 'padron': data, 'title':'Beneficiarios por localidad','detalle':localidad,'url':url}
    template = 'home/padron.html' if localidad else 'home/localidades.html'
    return render(request, template, context)

def descargas_empresa(request):
    data = get_descargas_por_empresa(request.user)
    context = { 'descargas': data, 'title':'Descargas por ciudad y empresa'}
    return render(request, 'home/empresas.html', context)

def grupo_familiar(request, dni = None):
    data = get_grupo_familiar(request.user, dni) if dni else get_grupo_familiar(request.user)
    template = 'home/grupo_familiar_detalle.html' if dni else 'home/grupo_familiar.html'
    context = { 'data': data, 'title':'Grupo familiar'}
    return render(request, template, context)

def cantidad_envases(request, tipo = None):
    data = get_cantidad_envases(request.user)
    template = 'home/envases_cantidad.html'
    context = { 'data': data, 'title':'Envases asignados'}
    return render(request, template, context)

@login_required(login_url="/login/")
@user_passes_test(is_agente)
def otras_consultas(request):
    return render(request, 'home/otras_consultas.html',{'title':'Otras consultas'})

def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))
