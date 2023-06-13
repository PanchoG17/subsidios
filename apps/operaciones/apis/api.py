from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from django.db.models import Q, Sum, Subquery, Count, Value, Case, When, CharField

from apps.operaciones.models import Conimpcub, Padben, Padbenfamiliares
from apps.operaciones.apis.serializers import PadBenSerializer, ConimpcubSerializer, GrupoFamiliarSerializer

import arrow

"""
Los períodos inician los días 29 de cada mes y finalizan los días 28(*)

En años bisiestos hay una excepción ya que el período inicia el 01 de marzo

La carga mensual se asigna el día 29 de cada mes y su periodo es el mes siguiente
ejemplo: las cargas mensuales de noviembre del 2022 deberían tener,
Fecha de transacción: 2022-10-29 y Periodo 01-11-2022
"""


# Consultas a tabla Conimpcub

"""
Este método devuelve todas las operaciones de CARGA, DESCARGA Y DEVOLUCIONES(CARGAS FUERA DE TERMINO)
por DNI del beneficiario en el mes actual (filtra por periodo de descarga)
"""
# SERIALIZER = ConimpcubSerializer
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def operaciones_mes_actual_api_view(request, dni=None):

    periodo_actual = arrow.now().ceil('month').date()
    periodo_operacion = str(periodo_actual.year) +'-'+ str(periodo_actual.month)+'-'+'01'

    if request.method == 'GET':
        operaciones = Conimpcub.objects.all().filter(
            conimpcubdni=dni).filter(
                conimpcubtipope__in =[
                    'CARGA MENSUAL',
                    'DESCARGA',
                    'DEVOL'
                    ]
                ).filter(
                    conimpcubperdes=periodo_operacion
                # ).order_by('-conimpcubfchtrn') # Orden descendente
                ).filter(
                    conimpcubanu='NO'
                ).order_by('conimpcubfchtrn')

        operaciones_serializer = ConimpcubSerializer(operaciones, many=True)
        return Response(operaciones_serializer.data)


"""
Este método devuelve todas las operaciones de CARGA, DESCARGA Y DEVOLUCIONES(CARGAS FUERA DE TERMINO)
por DNI del beneficiario del mes anterior(filtra por periodo de descarga)
"""
# SERIALIZER = ConimpcubSerializer
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def operaciones_mes_anterior_api_view(request, dni=None):

    periodo_anterior = arrow.now().shift(months=-1).ceil('month').date()
    periodo_operacion = str(periodo_anterior.year) +'-'+ str(periodo_anterior.month)+'-'+'01'

    if request.method == 'GET':

        operaciones = Conimpcub.objects.all().filter(
            conimpcubdni=dni).filter(
                conimpcubtipope__in =[
                    'CARGA MENSUAL',
                    'DESCARGA',
                    'DEVOL'
                    ]
                ).filter(
                    conimpcubperdes=periodo_operacion
                ).filter(
                    conimpcubanu='NO'
                ).order_by('conimpcubfchtrn')

        operaciones_serializer = ConimpcubSerializer(operaciones, many=True)
        return Response(operaciones_serializer.data)


"""
Este método devuelve todas las operaciones de DESCARGA realizadas por un beneficiario
en los ultimos 3 meses incluido el mes actual

o recibe por parametros el periodo a consultar (desde - hasta)
"""
# SERIALIZER = ConimpcubSerializer
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def operaciones_dos_meses_atras_api_view(request, dni=None, desde=None, hasta=None):

    if desde and hasta:
        desde = desde.split('-')
        hasta = hasta.split('-')
        periodo_anterior_operacion = str(desde[0]) +'-'+ str(desde[1])+'-'+'01'
        periodo_actual_operacion = str(hasta[0]) +'-'+ str(hasta[1])+'-'+'01'
    else:
        periodo_anterior = arrow.now().shift(months=-2).ceil('month').date()
        periodo_actual = arrow.now().ceil('month').date()
        periodo_anterior_operacion = str(periodo_anterior.year) +'-'+ str(periodo_anterior.month)+'-'+'01'
        periodo_actual_operacion = str(periodo_actual.year) +'-'+ str(periodo_actual.month)+'-'+'01'

    if request.method == 'GET':
        operaciones = Conimpcub.objects.all().filter(
            conimpcubdni=dni).filter(
                conimpcubtipope__in =[
                    'CARGA MENSUAL',
                    'DESCARGA',
                    'DEVOL'
                    ]
                ).filter(
                    conimpcubperdes__range = [periodo_anterior_operacion, periodo_actual_operacion]
                ).order_by('-conimpcubfchtrn')

        operaciones_serializer = ConimpcubSerializer(operaciones, many=True)
        return Response(operaciones_serializer.data)


"""
Este método devuelve las operaciones de CARGA Y DEVOLUCIONES(CARGAS FUERA DE TERMINO)
por DNI del beneficiario en el mes actual (filtra por periodo de descarga)
"""
# SERIALIZER = ConimpcubSerializer
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def asignacion_por_dni_api_view(request, dni=None):

    periodo_actual = arrow.now().ceil('month').date()
    periodo_operacion = str(periodo_actual.year) +'-'+ str(periodo_actual.month)+'-'+'01'

    if request.method == 'GET':

        cargas = Conimpcub.objects.all().filter(conimpcubdni=dni).filter(
            conimpcubperdes=periodo_operacion).filter(
            Q(conimpcubtipope='CARGA MENSUAL')| Q(conimpcubtipope__contains ='DEVOL'))

        cargas_serializer = ConimpcubSerializer(cargas, many=True)
        return Response(cargas_serializer.data)


"""
Este método devuelve las DESCARGAS
por DNI del beneficiario en el mes actual (filtra por periodo de descarga)
"""
# SERIALIZER = ConimpcubSerializer
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def descargas_por_dni_api_view(request, dni=None):

    periodo_actual = arrow.now().ceil('month').date()
    periodo_operacion = str(periodo_actual.year) +'-'+ str(periodo_actual.month)+'-'+'01'
    if request.method == 'GET':

        descargas = Conimpcub.objects.filter(
            conimpcubdni=dni,
            conimpcubperdes=periodo_operacion,
            conimpcubtipope='DESCARGA',
            conimpcubanu='NO'
        ).order_by('-conimpcubfchtrn')

        descargas_serializer = ConimpcubSerializer(descargas, many=True)
        response = descargas_serializer.data if descargas_serializer is not None else None
        return Response(response)

"""
Este método devuelve el último  SALDO
por DNI del beneficiario en el mes actual (filtra por periodo de descarga)
"""
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def saldos_api_view(request, dni=None):

    periodo_actual = arrow.now().ceil('month').date()
    periodo_operacion = str(periodo_actual.year) +'-'+ str(periodo_actual.month)+'-'+'01'
    response = None

    if request.method == 'GET':

        ops = Conimpcub.objects.filter(Q(conimpcubtipope='CARGA MENSUAL')|Q(conimpcubtipope__contains ='DEVOL')|Q(conimpcubtipope__contains ='DESCARGA'),conimpcubdni=dni,conimpcubperdes=periodo_operacion)
        if ops:
            response = {
                'dni' : ops[0].conimpcubdni,
                'beneficiario' : ops[0].conimpcubapenom.strip(),
                'localidad' : ops[0].conimpcubloc.strip(),
                'saldo' : 0
            }
            for o in ops:
                response['saldo'] += o.conimpcubcandes

        return Response(response)



##### Consultas a tabla PadBen #####

"""
Este método devuelve el padrón de todos los beneficiarios activos.
"""
# SERIALIZER = PadBenSerializer
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def padron_beneficiarios_api_view(request):

    if request.method == 'GET':
        try:
            beneficiarios_activos = Padben.objects.filter(
                (Q(padbenrazbaja ='')|Q(padbenrazbaja__isnull=True)),
                (Q(padbenfecbaja__isnull=True)|Q(padbenfecbaja='1753-01-01 00:00:00'))
            )[:15]

            beneficiarios_activos_serializer = PadBenSerializer(beneficiarios_activos, many=True)
            return Response(beneficiarios_activos_serializer.data)

        except:
            pass

"""
Este método devuelve el padrón de todos los beneficiarios inactivos de los últimos 2 meses.
"""
# SERIALIZER = PadBenSerializer
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def padron_sin_consumo_api_view(request, desde=None):

    if desde:
        desde = desde.split('-')
        periodo_anterior_operacion = str(desde[0]) +'-'+ str(desde[1])+'-'+'01'
    else:
        periodo_anterior = arrow.now().shift(months=-2).ceil('month').date()
        periodo_anterior_operacion = str(periodo_anterior.year) +'-'+ str(periodo_anterior.month)+'-'+'01'

    periodo_actual = arrow.now().ceil('month').date()
    periodo_actual_operacion = str(periodo_actual.year) +'-'+ str(periodo_actual.month)+'-'+'01'

    if request.method == 'GET':
        try:

            consumo_beneficiario = Conimpcub.objects.values_list('conimpcubdni').filter(
                    conimpcubperdes__range = [periodo_anterior_operacion, periodo_actual_operacion],
                    conimpcubtipope='DESCARGA').distinct()

            pad_sin_descargas = Padben.objects.filter(
                                    (Q(padbenrazbaja ='')|Q(padbenrazbaja__isnull=True)),
                                    (Q(padbenfecbaja__isnull=True)|Q(padbenfecbaja='1753-01-01 00:00:00')),
                                    (Q(padbenfecalt__lte = periodo_anterior_operacion)),
                                    (Q(padbenfecact__lte = periodo_anterior_operacion))
                                ).exclude(padbennrodoc__in=consumo_beneficiario)

            pad_sin_descargas_serializer = PadBenSerializer(pad_sin_descargas, many=True)
            response = pad_sin_descargas_serializer.data if pad_sin_descargas_serializer is not None else None

            return Response(response)

        except:

            pass



"""
Este método devuelve si el usuario es activo para validar al registrar un usuario
"""
@api_view(['GET'])
# SERIALIZER = PadBenSerializer
def beneficiario_api_view(request, dni=None):

    if request.method == 'GET':
        try:
            beneficiario = list(Padben.objects.all().filter(
                padbennrodoc=dni).filter(
                (Q(padbenrazbaja ='')|Q(padbenrazbaja__isnull=True)),
                (Q(padbenfecbaja__isnull=True)|Q(padbenfecbaja='1753-01-01 00:00:00')))
            )

            beneficiario_serializer = PadBenSerializer(beneficiario, many=True)

            return Response(beneficiario_serializer.data)

        except:

            pass


### Este método devuelve la cantidad de familiares declarados
### O devuelve detalle de familiares si recibe DNI
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def grupo_familiar_api_view(request, dni=None):
    if request.method == 'GET':
        if dni:
            try:
                grupo_familiar = Padbenfamiliares.objects.filter(padbennrodoc=dni).order_by('padbenfamtipo', 'padbenfamedad')
                grupo_familiar_serializer = GrupoFamiliarSerializer(grupo_familiar, many=True)
                return Response(grupo_familiar_serializer.data)
            except Exception as e:
                return Response(str(e))
        else:
            try:
                grupo_familiar = Padbenfamiliares.objects.values('padbennrodoc').annotate(count= Count('padbennrodoc')).order_by('-count')
                return Response(grupo_familiar)
            except Exception as e:
                return Response(str(e))

#### Este método devuelve los beneficiarios según el tipo de envase asignado para el último periodo
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def beneficiarios_por_envase_api_view(request, tipo = None):
    if request.method == 'GET':
        periodo_actual = arrow.now().ceil('month').date()
        periodo_operacion = str(periodo_actual.year) +'-'+ str(periodo_actual.month)+'-'+'01'

        if tipo:
            try:
                asignados = Conimpcub.objects.values('conimpcubdni').filter(
                    conimpcubperdes = periodo_operacion,
                    conimpcubtipope__in =['CARGA MENSUAL','DEVOL'],
                    conimpcubenvtip = tipo
                ).exclude(conimpcubcandes='0')
                beneficiarios = Padben.objects.filter(padbennrodoc__in=asignados)
                beneficiario_serializer = PadBenSerializer(beneficiarios, many=True)

                return Response(beneficiario_serializer.data)

            except Exception as e:
                return Response(str(e))
        else:
            try:
                asignados = Conimpcub.objects.values('conimpcubenvtip').filter(
                    conimpcubperdes = periodo_operacion,
                    conimpcubtipope__in =['CARGA MENSUAL','DEVOL'],
                ).exclude(conimpcubcandes='0'
                ).annotate(count = Count('conimpcubdni', distinct=True)
                ).annotate(envase = Case(
                    When(conimpcubenvtip=1, then=Value('Garrafa 10 KG')),
                    When(conimpcubenvtip=2, then=Value('Tubo 45 KG')),
                    When(conimpcubenvtip=3, then=Value('Granel')),
                    When(conimpcubenvtip=4, then=Value('Garrafa 15 KG')),
                    default=Value('Tubo 30 KG'),output_field=CharField())
                ).order_by('-count')
                return Response(asignados)

            except Exception as e:
                return Response(str(e))


### Este método devuelve los beneficiarios por barrio
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def beneficiarios_por_barrio_api_view(request, barrio=None):
    if request.method == 'GET':

        if barrio:
            try:
                beneficiarios = Padben.objects.filter(
                    (Q(padbenrazbaja ='')|Q(padbenrazbaja__isnull=True)),
                    (Q(padbenfecbaja__isnull=True)|Q(padbenfecbaja='1753-01-01 00:00:00')),
                    padbenbarrio = barrio
                ).order_by('padbenape')

                beneficiario_serializer = PadBenSerializer(beneficiarios, many=True)
                return Response(beneficiario_serializer.data)

            except Exception as e:
                return Response(str(e))
        else:
            try:
                beneficiarios = Padben.objects.values('padbenbarrio').filter(
                    (Q(padbenrazbaja ='')|Q(padbenrazbaja__isnull=True)),
                    (Q(padbenfecbaja__isnull=True)|Q(padbenfecbaja='1753-01-01 00:00:00'))
                ).annotate(count= Count('padbenbarrio')).order_by('-count')
                return Response(beneficiarios)

            except Exception as e:
                return Response(str(e))



### Este método devuelve los beneficiarios por localidad
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def beneficiarios_por_localidad_api_view(request, localidad=None):
    if request.method == 'GET':

        if localidad:
            try:
                beneficiarios = Padben.objects.order_by('padbenloc').filter(
                    (Q(padbenrazbaja ='')|Q(padbenrazbaja__isnull=True)),
                    (Q(padbenfecbaja__isnull=True)|Q(padbenfecbaja='1753-01-01 00:00:00')),
                    padbenloc = localidad
                ).order_by('padbenloc')

                beneficiario_serializer = PadBenSerializer(beneficiarios, many=True)
                return Response(beneficiario_serializer.data)

            except Exception as e:
                return Response(str(e))
        else:
            try:
                beneficiarios = Padben.objects.values('padbenloc').order_by('padbenloc').filter(
                    (Q(padbenrazbaja ='')|Q(padbenrazbaja__isnull=True)),
                    (Q(padbenfecbaja__isnull=True)|Q(padbenfecbaja='1753-01-01 00:00:00'))
                ).annotate(localidad= Count('padbenloc')).order_by('-localidad')

                for b in beneficiarios:
                    b['padbenloc'] = b['padbenloc'].strip()

                return Response(beneficiarios)

            except Exception as e:
                return Response(str(e))


### Este método devuelve la cantidad de envases y la suma de kilogramos asignados por c/u
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def cantidad_envases_api_view(request):

    if request.method == 'GET':

        try:
            periodo_actual = arrow.now().ceil('month').date()
            periodo_operacion = str(periodo_actual.year) +'-'+ str(periodo_actual.month)+'-'+'01'

            envases = Conimpcub.objects.values('conimpcubenvtip').filter(
                conimpcubperdes = periodo_operacion,
                conimpcubtipope__in =['CARGA MENSUAL','DEVOL']
            ).exclude(conimpcubcandes='0'
            ).annotate(count= Sum('conimpcubcandes') / Case(
                When(conimpcubenvtip=1, then=Value(10)),
                When(conimpcubenvtip=2, then=Value(45)),
                When(conimpcubenvtip=4, then=Value(15)),
                When(conimpcubenvtip=5, then=Value(30)),
            )).annotate(envase = Case(
                When(conimpcubenvtip=1, then=Value('Garrafa 10 KG')),
                When(conimpcubenvtip=2, then=Value('Tubo 45 KG')),
                When(conimpcubenvtip=3, then=Value('Granel')),
                When(conimpcubenvtip=4, then=Value('Garrafa 15 KG')),
                default=Value('Tubo 30 KG'),output_field=CharField()
            )).annotate(kilos= Sum('conimpcubcandes')).order_by('-count')

            ## VALIDACIÓN PARA NUEVOS PERIODOS SIN ASIGNACIONES
            if not envases:
                envases = [
                    {'conimpcubenvtip':0,'envase':'Garrafa 10KG','count':0,'kilos':0},
                    {'conimpcubenvtip':0,'envase':'Garrafa 15KG','count':0,'kilos':0},
                    {'conimpcubenvtip':0,'envase':'Tubo 30KG','count':0,'kilos':0},
                    {'conimpcubenvtip':0,'envase':'Tubo 45KG','count':0,'kilos':0},
                    {'conimpcubenvtip':0,'envase':'Granel','count':0,'kilos':0},
                ]

            return Response(envases)

        except Exception as e:
            return Response(str(e))


### Este método devuelve los kilogramos descargados por ciudad y por empresa
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def descargas_por_empresa_api_view(request):

    if request.method == 'GET':

        periodo_actual = arrow.now().ceil('month').date()
        periodo_operacion = str(periodo_actual.year) +'-'+ str(periodo_actual.month)+'-'+'01'

        try:
            descargas = Conimpcub.objects.values('conimpcubloc','conimpcubcomnom').filter(
                conimpcubperdes = periodo_operacion,
                conimpcubtipope = 'DESCARGA'
            ).annotate(kilos = Sum('conimpcubcandes')).order_by('conimpcubloc')

            return Response(descargas)

        except Exception as e:
            return Response(str(e))