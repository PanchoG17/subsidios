from rest_framework import serializers
import locale

from apps.operaciones.models import Conimpcub, Padben, Padbenfamiliares, Verificacub
# locale.setlocale(locale.LC_ALL, 'es-es.UTF-8')

class VerificacubSerializer(serializers.ModelSerializer):
    dni = serializers.CharField(source='verificacubdni')
    localidad = serializers.CharField(source= 'verificacubloc')
    fecha_trn = serializers.CharField(source='verificacubfchtrn')
    beneficiario = serializers.CharField(source='verificacubapenom')
    operacion = serializers.CharField(source='verificacubtipope')
    envase = serializers.CharField(source='verificacubenvtip')
    comercio = serializers.CharField(source='verificacubcomercio')
    asignacion = serializers.CharField(source='verificacubcntasignada')
    cantidad_descargada = serializers.CharField(source='verificacubcntdescargada')
    periodo = serializers.CharField(source='verificacubperdes')
    saldo = serializers.CharField(source='verificacubsaldo')

    class Meta:
        model = Verificacub
        fields = ['dni','localidad','fecha_trn','beneficiario','operacion','envase','comercio','saldo','asignacion','cantidad_descargada','periodo']

    def to_representation(self, instance):

        if instance.verificacubenvtip == 1:
            envase='Garrafa 10kg.'
        elif instance.verificacubenvtip == 2:
            envase='Tubo 45kg.'
        elif instance.verificacubenvtip == 3:
            envase='Granel'
        elif instance.verificacubenvtip == 4:
            envase='Garrafa 15kg.'
        else:
            envase='Tubo 30kg.'

        return {
            'dni' : instance.verificacubdni,
            'beneficiario' : instance.verificacubapenom.strip(),
            'localidad' : instance.verificacubloc.strip(),
            'fecha_trn' : instance.verificacubfchtrn.date(),
            'operacion' : instance.verificacubtipope.strip(),
            'envase' : envase,
            'comercio' : instance.verificacubcomercio.strip(),
            'asignacion' : instance.verificacubcntasignada,
            'cantidad_descargada' : instance.verificacubcntdescargada,
            'periodo' : instance.verificacubperdes.strftime("%B").title(),
            'saldo' : instance.verificacubsaldo
        }

class VerificacubSaldoSerializer(serializers.ModelSerializer):
    localidad = serializers.CharField(source='verificacubloc')
    #beneficiario = serializers.CharField(source='verificacubapenom')
    saldo = serializers.CharField(source='verificacubsaldo')
    dni = serializers.CharField(source='verificacubdni')

    class Meta:
        model = Verificacub
        fields = ['dni','localidad','beneficiario','saldo']

    def to_representation(self, instance):
        return {
            'dni' : instance.verificacubdni,
            #'beneficiario' : instance.verificacubapenom.strip(),
            'localidad' : instance.verificacubloc.strip(),
            'saldo' : instance.verificacubsaldo
        }

class ConimpcubSerializer(serializers.ModelSerializer):
    dni = serializers.CharField(source='conimpcubdni')
    localidad = serializers.CharField(source= 'conimpcubloc')
    fecha_trn = serializers.CharField(source='conimpcubfchtrn')
    #beneficiario = serializers.CharField(source='conimpcubapenom')
    operacion = serializers.CharField(source='conimpcubtipope')
    envase = serializers.CharField(source='conimpcubenvtip')
    comercio = serializers.CharField(source='conimpcubcomnom')
    cantidad = serializers.CharField(source='conimpcubcandes')
    periodo = serializers.CharField(source='conimpcubperdes')

    class Meta:
        model = Conimpcub
        fields = ['dni','beneficiario','localidad','operacion','comercio','fecha_trn','envase','cantidad','periodo']

    def to_representation(self, instance):
        if instance.conimpcubenvtip == 1:
            envase='Garrafa 10kg.'
        elif instance.conimpcubenvtip == 2:
            envase='Tubo 45kg.'
        elif instance.conimpcubenvtip == 3:
            envase='Granel'
        elif instance.conimpcubenvtip == 4:
            envase='Garrafa 15kg.'
        else:
            envase='Tubo 30kg.'

        return {
            'dni' : instance.conimpcubdni,
            #'beneficiario' : instance.conimpcubapenom.strip(),
            'localidad' : instance.conimpcubloc.strip(),
            'fecha_trn' : instance.conimpcubfchtrn.date(),
            'periodo' : instance.conimpcubperdes.strftime("%B").title(),
            'operacion' : instance.conimpcubtipope.strip(),
            'cantidad' : instance.conimpcubcandes,
            'envase' : envase,
            'comercio' : instance.conimpcubcomnom.strip(),
        }

class PadBenSerializer(serializers.ModelSerializer):
    apellido = serializers.CharField(source='padbenape')
    nombre = serializers.CharField(source='padbennom')
    dni = serializers.CharField(source='padbennrodoc')
    localidad = serializers.CharField(source='padbenloc')
    barrio = serializers.CharField(source='padbenbarrio')
    domicilio = serializers.CharField(source='padbencal')
    cod_area = serializers.CharField(source='padbencaracteristicacelular')
    celular = serializers.CharField(source='padbencel')
    ultima_actualizacion = serializers.CharField(source='padbenfecact')

    class Meta:
        model = Padben
        fields = ['apellido','nombre','dni','localidad','domicilio','barrio','cod_area','celular','ultima_actualizacion']

    def to_representation(self, instance):

        try:
            if instance.padbendomcal is not None:
                dir = instance.padbendomcal.strip()+', ' if instance.padbendomcal.strip() else ''
            else:
                dir = ''

            if instance.padbendomnro and instance.padbendomnro != 0:
                dir += str(instance.padbendomnro) + ' '
            else:
                if instance.padbennrocasa.strip() and instance.padbennrocasa != 0:
                    dir += 'Casa ' + str(instance.padbennrocasa).strip() + ' '
                if instance.padbennrolote.strip() and instance.padbennrolote != 0:
                    dir += 'Lote ' + str(instance.padbennrolote).strip() + ' '
                if instance.padbennroparcela.strip() and instance.padbennroparcela != 0:
                    dir += 'Parcela ' + str(instance.padbennroparcela).strip() + ' '
                if instance.padbennromacizo.strip() and instance.padbennromacizo != 0:
                    dir += 'Macizo ' + str(instance.padbennromacizo).strip() + ' '
                if instance.padbennromanzana.strip() and instance.padbennromanzana != 0:
                    dir += 'Manzana ' + str(instance.padbennromanzana).strip() + ' '
        except Exception as e:
            #print(e)
            pass

        apellido = instance.padbenape.strip() if instance.padbenape is not None else '-'
        nombre = instance.padbennom.strip() if instance.padbennom is not None else '-'
        localidad = instance.padbenloc.strip() if instance.padbenloc is not None else '-'
        barrio = instance.padbenbarrio.strip() if instance.padbenbarrio is not None else '-'
        cod_area = instance.padbencaracteristicacelular.strip() if instance.padbencaracteristicacelular is not None else '-'
        celular = instance.padbencel.strip() if instance.padbencel is not None else '-'
        ultima_actualizacion = instance.padbenfecact.date() if instance.padbenfecact is not None else '-'

        return {
            'apellido': apellido,
            'nombre':nombre,
            'dni':instance.padbennrodoc,
            'localidad':localidad,
            'barrio':barrio,
            'domicilio': dir,
            'cod_area':cod_area,
            'celular':celular,
            'ultima_actualizacion':ultima_actualizacion,
        }

class GrupoFamiliarSerializer(serializers.ModelSerializer):
    apellido = serializers.CharField(source='padbenfamape')
    nombre = serializers.CharField(source='padbenfamnom')
    dni = serializers.CharField(source='padbenfamnrodoc')
    edad = serializers.CharField(source='padbenfamedad')
    parentesco = serializers.CharField(source='padbenfamtipo')
    ocupacion = serializers.CharField(source='padbenfamocu')

    class Meta:
        model = Padbenfamiliares
        fields = ['apellido','nombre','dni','edad','parentesco','ocupacion']

    def to_representation(self, instance):

        ocupacion = '-' if instance.padbenfamocu.strip() == 'Seleccionar' else instance.padbenfamocu
        return {
            'apellido': instance.padbenfamape.strip(),
            'nombre':instance.padbenfamnom.strip(),
            'dni':instance.padbenfamnrodoc,
            'edad':instance.padbenfamedad,
            'parentesco':instance.padbenfamtipo.rparentdsc.strip(),
            'ocupacion':ocupacion
        }