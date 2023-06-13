from zeep import Client
from zeep.transports import Transport
import urllib3
import requests

from rest_framework.authtoken.models import Token

session = requests.Session()
session.verify = False
transport = Transport(session=session)
cliente = Client('https://####', transport=transport)
URL_BASE = 'http://localhost:8000/'

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def ADWSLogin(username, password):
    # verificacion del usuario con AD
    try:
        is_user = cliente.service.Login(username, password)
        if is_user:
            return is_user
    except:
        return 'No hay datos para ' + username

def ADWSGetDni(username):
    # obtencion del documento del usuario
    try:
        dni = cliente.service.GetDni(username)

        return dni

    except:
        return 'No hay datos de DNI para ' + username

def ADWSGetUser(dni_usuario):
    try:
        usuario = cliente.service.GetUser(dni_usuario)

        return usuario

    except:
        return 'No hay datos para el dni ' + dni_usuario

def ADWSGetUsuarioYPass(username):
    try:
        datos = cliente.service.GetUsuarioYPass(username)
        return datos
    except:
        return 'No se han encontrado datos del usuario ' + username

def getEnvase(tipo):
    envases = {
        0:'',
        1:'Garrafa 10 KG',
        2:'Tubo 45 KG',
        3:'Granel',
        4:'Garrafa 15 KG',
        5:'Tubo 30 KG'
    }
    return envases[tipo]

##### API Django_REST Methods ######
def setToken(user, password):
    payload = dict(username=user, password=password)
    url = URL_BASE + 'consultas/auth/'
    requests.post(url, data=payload)

def getToken(user):
    try:
        token = Token.objects.get(user = user).key
    except:
        token = None
    return token

def getData(url, user = None):
    try:
        headers = {'Authorization': 'Token ' + getToken(user)} if user else None
        data = requests.get(url, headers=headers)
        data = data.json()
        return data
    except Exception as e:
        pass

def padron_beneficiarios(user):
    url = URL_BASE + 'consultas/padron_beneficiarios/'
    return getData(url, user)

def padron_sin_consumo(user, desde=None):
    url = URL_BASE + 'consultas/padron_sin_consumo/'+ desde +'/' if desde else URL_BASE + 'consultas/padron_sin_consumo/'
    return getData(url, user)

def es_beneficiario(documento):
    url = URL_BASE + 'consultas/beneficiario/' + str(documento) +'/'
    return getData(url)

def mes_actual(documento, user):
    url = URL_BASE + 'consultas/operaciones_mensuales/mes_actual/' + str(documento) +'/'
    return getData(url, user)

def mes_anterior(documento, user):
    url = URL_BASE + 'consultas/operaciones_mensuales/mes_anterior/' + str(documento) +'/'
    return getData(url, user)

def dos_meses_anteriores(documento,user):
    url = URL_BASE + 'consultas/operaciones_mensuales/dos_meses_atras/' + str(documento) +'/'
    return getData(url, user)

def consumo_extendido(documento, user, desde=None, hasta=None):
    url = URL_BASE + 'consultas/operaciones_mensuales/consumo_extendido/' + str(documento) +'/'+ desde+'/'+ hasta+'/'
    return getData(url, user)

def asignacion(documento, user):
    url = URL_BASE + 'consultas/operaciones_mensuales/asignacion/' + str(documento) +'/'
    return getData(url, user)

def descarga(documento, user):
    url = URL_BASE + 'consultas/operaciones_mensuales/descarga/' + str(documento) +'/'
    return getData(url, user)

def saldo(documento, user):
    url = URL_BASE + 'consultas/operaciones_mensuales/saldo/' + str(documento) +'/'
    return getData(url, user)

## Otras consultas
def get_cantidad_envases(user):
    url = URL_BASE + 'consultas/cantidad_envases'+'/'
    return getData(url, user)

def get_beneficiarios_por_barrio(user, barrio=None):
    url = URL_BASE + 'consultas/beneficiarios_por_barrio/' + str(barrio) + '/' if barrio else URL_BASE + 'consultas/beneficiarios_por_barrio/'
    return getData(url, user)

def get_beneficiarios_por_localidad(user, localidad=None):
    url = URL_BASE + 'consultas/beneficiarios_por_localidad/' + str(localidad) + '/' if localidad else URL_BASE + 'consultas/beneficiarios_por_localidad/'
    return getData(url, user)

def get_beneficiarios_por_envase(user,tipo = None):
    url = URL_BASE + 'consultas/beneficiarios_por_envase/'+ str(tipo) +'/' if tipo else URL_BASE + 'consultas/beneficiarios_por_envase/'
    return getData(url, user)

def get_descargas_por_empresa(user):
    url = URL_BASE + 'consultas/descargas_por_empresa/'
    return getData(url, user)

def get_grupo_familiar(user, dni=None):
    url = URL_BASE + 'consultas/grupo_familiar/'+ str(dni) +'/' if dni else URL_BASE + 'consultas/grupo_familiar/'
    return getData(url, user)