# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Archivocsv(models.Model):
    arccsvnrodoc = models.CharField(db_column='ArcCSVNroDoc', max_length=20)  # Field name made lowercase.
    arccsvtipdoc = models.CharField(db_column='ArcCSVTipDoc', max_length=20)  # Field name made lowercase.
    arccsvnomben = models.CharField(db_column='ArcCSVNomBen', max_length=40)  # Field name made lowercase.
    arccsvlugnacben = models.CharField(db_column='ArcCSVLugNacBen', max_length=40)  # Field name made lowercase.
    arccsvbarben = models.CharField(db_column='ArcCSVBarBen', max_length=40)  # Field name made lowercase.
    arccsvdirdomben = models.CharField(db_column='ArcCSVDirDomBen', max_length=150)  # Field name made lowercase.
    arccsvfchnacben = models.CharField(db_column='ArcCSVFchNacBen', max_length=20)  # Field name made lowercase.
    arccsvnacben = models.CharField(db_column='ArcCSVNacBen', max_length=40)  # Field name made lowercase.
    arccsvestcivben = models.CharField(db_column='ArcCSVEstCivBen', max_length=20)  # Field name made lowercase.
    arccsvfchresben = models.CharField(db_column='ArcCSVFchResBen', max_length=20)  # Field name made lowercase.
    arccsvzongeoben = models.CharField(db_column='ArcCSVZonGeoBen', max_length=20)  # Field name made lowercase.
    arcfchpaspad = models.DateTimeField(db_column='ArcFchPasPad')  # Field name made lowercase.
    arcexp = models.BooleanField(db_column='ArcExp')  # Field name made lowercase.
    arccsvlocalidad = models.CharField(db_column='ArcCSVLocalidad', max_length=20)  # Field name made lowercase.
    arcfchbajpad = models.DateTimeField(db_column='ArcFchBajPad')  # Field name made lowercase.
    arccsvfchimp = models.DateTimeField(db_column='ArcCSVFchImp')  # Field name made lowercase.
    arccsvfchexp = models.DateTimeField(db_column='ArcCSVFchExp')  # Field name made lowercase.
    arccsvimp = models.BooleanField(db_column='ArcCSVImp')  # Field name made lowercase.
    arccsvcntsol = models.SmallIntegerField(db_column='ArcCSVCntSol')  # Field name made lowercase.
    arccsvtipenv = models.SmallIntegerField(db_column='ArcCSVTipEnv')  # Field name made lowercase.
    arccsvid = models.AutoField(db_column='ArcCSVId', primary_key=True)  # Field name made lowercase.
    arccsvbennrodoc = models.ForeignKey('Padben', models.DO_NOTHING, db_column='ArcCSVBenNroDoc', blank=True, null=True)  # Field name made lowercase.
    arccsvreactivado = models.BooleanField(db_column='ArcCSVReactivado')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ArchivoCSV'


class Asignacionpersona(models.Model):
    asiperid = models.AutoField(db_column='AsiPerId', primary_key=True)  # Field name made lowercase.
    asipernrodoc = models.IntegerField(db_column='AsiPerNroDoc', blank=True, null=True)  # Field name made lowercase.
    asiperape = models.CharField(db_column='AsiPerApe', max_length=60, blank=True, null=True)  # Field name made lowercase.
    asipernom = models.CharField(db_column='AsiPerNom', max_length=60, blank=True, null=True)  # Field name made lowercase.
    asitotalkg = models.SmallIntegerField(db_column='AsiTotalKg', blank=True, null=True)  # Field name made lowercase.
    benid = models.ForeignKey('Djbenfam', models.DO_NOTHING, db_column='BenId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AsignacionPersona'


class Asignacionpersonatipocantidad(models.Model):
    asiperid = models.OneToOneField(Asignacionpersona, models.DO_NOTHING, db_column='AsiPerId', primary_key=True)  # Field name made lowercase.
    asitipcod = models.ForeignKey('Asignaciontipo', models.DO_NOTHING, db_column='AsiTipCod')  # Field name made lowercase.
    asitipcntsol = models.SmallIntegerField(db_column='AsiTipCntSol', blank=True, null=True)  # Field name made lowercase.
    asitipcntsolkg = models.SmallIntegerField(db_column='AsiTipCntSolKg', blank=True, null=True)  # Field name made lowercase.
    asitipfchsol = models.DateTimeField(db_column='AsiTipFchSol', blank=True, null=True)  # Field name made lowercase.
    assubtotal = models.IntegerField(db_column='ASSubtotal', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AsignacionPersonaTipoCantidad'
        unique_together = (('asiperid', 'asitipcod'),)


class Asignaciontipo(models.Model):
    asitipcod = models.AutoField(db_column='AsiTipCod', primary_key=True)  # Field name made lowercase.
    asitipdes = models.CharField(db_column='AsiTipDes', max_length=40)  # Field name made lowercase.
    asitipcntkg = models.SmallIntegerField(db_column='AsiTipCntKg')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AsignacionTipo'


class Auditoria(models.Model):
    audid = models.AutoField(db_column='AudID', primary_key=True)  # Field name made lowercase.
    audobjinv = models.CharField(db_column='AudObjInv', max_length=60)  # Field name made lowercase.
    audusrlog = models.CharField(db_column='AudUsrLog', max_length=25)  # Field name made lowercase.
    audusrnam = models.CharField(db_column='AudUsrNam', max_length=40)  # Field name made lowercase.
    audusrape = models.CharField(db_column='AudUsrApe', max_length=40)  # Field name made lowercase.
    audfchope = models.DateTimeField(db_column='AudFchOpe')  # Field name made lowercase.
    audtipopedel = models.BooleanField(db_column='AudTipOpeDel')  # Field name made lowercase.
    audtipopeins = models.BooleanField(db_column='AudTipOpeIns')  # Field name made lowercase.
    audtipopeupd = models.BooleanField(db_column='AudTipOpeUpd')  # Field name made lowercase.
    audtipopesc = models.BooleanField(db_column='AudTipOpeSC')  # Field name made lowercase.
    audtipope = models.CharField(db_column='AudTipOpe', max_length=40)  # Field name made lowercase.
    auddestipope = models.CharField(db_column='AudDesTipOpe', max_length=200)  # Field name made lowercase.
    audacept = models.BooleanField(db_column='AudAcept')  # Field name made lowercase.
    audrech = models.BooleanField(db_column='AudRech')  # Field name made lowercase.
    audddjjdoc = models.IntegerField(db_column='AudDDJJDoc')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Auditoria'


class Barrios(models.Model):
    barcod = models.AutoField(db_column='BarCod', primary_key=True)  # Field name made lowercase.
    bardes = models.CharField(db_column='BarDes', max_length=80)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Barrios'


class Calle(models.Model):
    calcodsig = models.IntegerField(db_column='CalCodSig', primary_key=True)  # Field name made lowercase.
    calnom = models.CharField(db_column='CalNom', max_length=80)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Calle'


class Cantidad(models.Model):
    cantid = models.AutoField(db_column='CantID', primary_key=True)  # Field name made lowercase.
    candoc = models.ForeignKey('Padben', models.DO_NOTHING, db_column='CanDoc', blank=True, null=True)  # Field name made lowercase.
    cantipo = models.SmallIntegerField(db_column='CanTipo', blank=True, null=True)  # Field name made lowercase.
    cankg = models.SmallIntegerField(db_column='CanKg', blank=True, null=True)  # Field name made lowercase.
    canfchvig = models.DateTimeField(db_column='CanFchVig', blank=True, null=True)  # Field name made lowercase.
    canmar = models.CharField(db_column='CanMar', max_length=1, blank=True, null=True)  # Field name made lowercase.
    candefinitiva = models.SmallIntegerField(db_column='CanDefinitiva', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Cantidad'


class Cantidad2(models.Model):
    can2tid = models.AutoField(db_column='Can2tID', primary_key=True)  # Field name made lowercase.
    can2doc = models.IntegerField(db_column='Can2Doc', blank=True, null=True)  # Field name made lowercase.
    can2tipo = models.SmallIntegerField(db_column='Can2Tipo', blank=True, null=True)  # Field name made lowercase.
    can2kg = models.SmallIntegerField(db_column='Can2Kg', blank=True, null=True)  # Field name made lowercase.
    can2fchvig = models.DateTimeField(db_column='Can2FchVig', blank=True, null=True)  # Field name made lowercase.
    can2mar = models.CharField(db_column='Can2Mar', max_length=1, blank=True, null=True)  # Field name made lowercase.
    can2definitiva = models.SmallIntegerField(db_column='Can2Definitiva', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Cantidad2'


class Ciudades(models.Model):
    ciuid = models.IntegerField(db_column='CiuId', primary_key=True)  # Field name made lowercase.
    ciudes = models.CharField(db_column='CiuDes', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Ciudades'


class Ciudadesbarrio(models.Model):
    ciuid = models.OneToOneField(Ciudades, models.DO_NOTHING, db_column='CiuId', primary_key=True)  # Field name made lowercase.
    ciubarcod = models.ForeignKey(Barrios, models.DO_NOTHING, db_column='CiuBarCod')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CiudadesBarrio'
        unique_together = (('ciuid', 'ciubarcod'),)


class Conimpcub(models.Model):
    conimpcubid = models.AutoField(db_column='ConImpCubId', primary_key=True)  # Field name made lowercase.
    conimpcubloc = models.CharField(db_column='ConImpCubLoc', max_length=20, blank=True, null=True)  # Field name made lowercase.
    conimpcubfchtrn = models.DateTimeField(db_column='ConImpCubFchTrn', blank=True, null=True)  # Field name made lowercase.
    conimpcubhratrn = models.CharField(db_column='ConImpCubHraTrn', max_length=20, blank=True, null=True)  # Field name made lowercase.
    conimpcubidtrngob = models.IntegerField(db_column='ConImpCubIdTrnGob', blank=True, null=True)  # Field name made lowercase.
    conimpcubdni = models.IntegerField(db_column='ConImpCubDni', blank=True, null=True)  # Field name made lowercase.
    conimpcubapenom = models.CharField(db_column='ConImpCubApeNom', max_length=40, blank=True, null=True)  # Field name made lowercase.
    conimpcubperdes = models.DateTimeField(db_column='ConImpCubPerDes', blank=True, null=True)  # Field name made lowercase.
    conimpcubenvtip = models.SmallIntegerField(db_column='ConImpCubEnvTip', blank=True, null=True)  # Field name made lowercase.
    conimpcubcandes = models.DecimalField(db_column='ConImpCubCanDes', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    conimpcubcomnom = models.CharField(db_column='ConImpCubComNom', max_length=20, blank=True, null=True)  # Field name made lowercase.
    conimpcubletctr = models.CharField(db_column='ConImpCubLetCtr', max_length=2, blank=True, null=True)  # Field name made lowercase.
    conimpcubtipope = models.CharField(db_column='ConImpCubTipOpe', max_length=20, blank=True, null=True)  # Field name made lowercase.
    conimpcubanu = models.CharField(db_column='ConImpCubAnu', max_length=2, blank=True, null=True)  # Field name made lowercase.
    conimpcubfchimp = models.DateTimeField(db_column='ConImpCubFchImp', blank=True, null=True)  # Field name made lowercase.
    conimpcubusrimp = models.CharField(db_column='ConImpCubUsrImp', max_length=20, blank=True, null=True)  # Field name made lowercase.
    conimpcubhash = models.CharField(db_column='ConImpCubHash', max_length=32, blank=True, null=True)  # Field name made lowercase.
    conimpcubdom = models.CharField(db_column='ConImpCubDom', max_length=150)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ConImpCub'

    def __str__(self):
        return '{}'.format(
            self.conimpcubapenom,
        )


class Conimptar(models.Model):
    conimptarid = models.AutoField(db_column='ConImpTarId', primary_key=True)  # Field name made lowercase.
    conimptaridcom = models.IntegerField(db_column='ConImpTarIdCom', blank=True, null=True)  # Field name made lowercase.
    conimptarcodprd = models.IntegerField(db_column='ConImpTarCodPrd', blank=True, null=True)  # Field name made lowercase.
    conimptarfchtrn = models.DateTimeField(db_column='ConImpTarFchTrn', blank=True, null=True)  # Field name made lowercase.
    conimptarhratrn = models.CharField(db_column='ConImpTarHraTrn', max_length=20, blank=True, null=True)  # Field name made lowercase.
    conimptaridter = models.CharField(db_column='ConImpTarIdTer', max_length=20, blank=True, null=True)  # Field name made lowercase.
    conimptarcodaut = models.CharField(db_column='ConImpTarCodAut', max_length=20, blank=True, null=True)  # Field name made lowercase.
    conimptarlot = models.CharField(db_column='ConImpTarLot', max_length=20, blank=True, null=True)  # Field name made lowercase.
    conimptarnrocup = models.CharField(db_column='ConImpTarNroCup', max_length=20, blank=True, null=True)  # Field name made lowercase.
    conimptarcntenv = models.SmallIntegerField(db_column='ConImpTarCntEnv', blank=True, null=True)  # Field name made lowercase.
    conimptarcntdes = models.DecimalField(db_column='ConImpTarCntDes', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    conimptaranu = models.CharField(db_column='ConImpTarAnu', max_length=2, blank=True, null=True)  # Field name made lowercase.
    conimptartip = models.CharField(db_column='ConImpTarTip', max_length=20, blank=True, null=True)  # Field name made lowercase.
    conimptarnrotar = models.CharField(db_column='ConImpTarNroTar', max_length=20, blank=True, null=True)  # Field name made lowercase.
    conimptarapenom = models.CharField(db_column='ConImpTarApeNom', max_length=40, blank=True, null=True)  # Field name made lowercase.
    conimptardni = models.IntegerField(db_column='ConImpTarDNI', blank=True, null=True)  # Field name made lowercase.
    conimptarloc = models.CharField(db_column='ConImpTarLoc', max_length=20, blank=True, null=True)  # Field name made lowercase.
    conimptardom = models.CharField(db_column='ConImpTarDom', max_length=150, blank=True, null=True)  # Field name made lowercase.
    conimptaridtrngob = models.IntegerField(db_column='ConImpTarIdTrnGob', blank=True, null=True)  # Field name made lowercase.
    conimptarfchimp = models.DateTimeField(db_column='ConImpTarFchImp', blank=True, null=True)  # Field name made lowercase.
    conimptarusrimp = models.CharField(db_column='ConImpTarUsrImp', max_length=20, blank=True, null=True)  # Field name made lowercase.
    conimptarhash = models.CharField(db_column='ConImpTarHash', max_length=32, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ConImpTar'


class Controltarjeta(models.Model):
    contarid = models.AutoField(db_column='ConTarId', primary_key=True)  # Field name made lowercase.
    contarnrodoc = models.IntegerField(db_column='ConTarNroDoc', blank=True, null=True)  # Field name made lowercase.
    contarapenom = models.CharField(db_column='ConTarApeNom', max_length=40, blank=True, null=True)  # Field name made lowercase.
    contarnrotar = models.CharField(db_column='ConTarNroTar', max_length=20, blank=True, null=True)  # Field name made lowercase.
    contarvigdsd = models.DateTimeField(db_column='ConTarVigDsd', blank=True, null=True)  # Field name made lowercase.
    contarvighst = models.DateTimeField(db_column='ConTarVigHst', blank=True, null=True)  # Field name made lowercase.
    contaresttar = models.CharField(db_column='ConTarEstTar', max_length=1, blank=True, null=True)  # Field name made lowercase.
    contarfchent = models.DateTimeField(db_column='ConTarFchEnt', blank=True, null=True)  # Field name made lowercase.
    contarusrent = models.CharField(db_column='ConTarUsrEnt', max_length=20, blank=True, null=True)  # Field name made lowercase.
    contarhash = models.CharField(db_column='ConTarHash', max_length=22, blank=True, null=True)  # Field name made lowercase.
    contarape = models.CharField(db_column='ConTarApe', max_length=20, blank=True, null=True)  # Field name made lowercase.
    contarnom = models.CharField(db_column='ConTarNom', max_length=25, blank=True, null=True)  # Field name made lowercase.
    contarfchimp = models.DateTimeField(db_column='ConTarFchImp', blank=True, null=True)  # Field name made lowercase.
    contarusrimp = models.CharField(db_column='ConTarUsrImp', max_length=20, blank=True, null=True)  # Field name made lowercase.
    contarhashent = models.CharField(db_column='ConTarHashEnt', max_length=22, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ControlTarjeta'


class Djbenfam(models.Model):
    benid = models.AutoField(db_column='BenId', primary_key=True)  # Field name made lowercase.
    bencuit = models.DecimalField(db_column='BenCuit', max_digits=11, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    bennrodoc = models.IntegerField(db_column='BenNroDoc', blank=True, null=True)  # Field name made lowercase.
    bennomape = models.CharField(db_column='BenNomApe', max_length=60, blank=True, null=True)  # Field name made lowercase.
    benlugnac = models.CharField(db_column='BenLugNac', max_length=40, blank=True, null=True)  # Field name made lowercase.
    bennac = models.ForeignKey('Rpais', models.DO_NOTHING, db_column='BenNac', blank=True, null=True)  # Field name made lowercase.
    bensexo = models.SmallIntegerField(db_column='BenSexo', blank=True, null=True)  # Field name made lowercase.
    benfecnac = models.DateTimeField(db_column='BenFecNac', blank=True, null=True)  # Field name made lowercase.
    bencivest = models.ForeignKey('Restciv', models.DO_NOTHING, db_column='BenCivEst', blank=True, null=True)  # Field name made lowercase.
    benrectmp = models.SmallIntegerField(db_column='BenRecTmp', blank=True, null=True)  # Field name made lowercase.
    benrectmpmed = models.SmallIntegerField(db_column='BenRecTmpMed', blank=True, null=True)  # Field name made lowercase.
    benloc = models.SmallIntegerField(db_column='BenLoc', blank=True, null=True)  # Field name made lowercase.
    benbario = models.CharField(db_column='BenBario', max_length=40, blank=True, null=True)  # Field name made lowercase.
    benzona = models.CharField(db_column='BenZona', max_length=20, blank=True, null=True)  # Field name made lowercase.
    bendomcal = models.CharField(db_column='BenDomCal', max_length=40, blank=True, null=True)  # Field name made lowercase.
    bendomnro = models.IntegerField(db_column='BenDomNro', blank=True, null=True)  # Field name made lowercase.
    bentel = models.CharField(db_column='BenTel', max_length=20, blank=True, null=True)  # Field name made lowercase.
    bencel = models.CharField(db_column='BenCel', max_length=20, blank=True, null=True)  # Field name made lowercase.
    benemail = models.CharField(db_column='BenEMail', max_length=100, blank=True, null=True)  # Field name made lowercase.
    benasigtipo = models.SmallIntegerField(db_column='BenAsigTipo', blank=True, null=True)  # Field name made lowercase.
    benobs = models.TextField(db_column='BenObs', blank=True, null=True)  # Field name made lowercase.
    benhash = models.CharField(db_column='BenHash', max_length=40, blank=True, null=True)  # Field name made lowercase.
    benestado = models.SmallIntegerField(db_column='BenEstado', blank=True, null=True)  # Field name made lowercase.
    benfecha = models.DateTimeField(db_column='BenFecha', blank=True, null=True)  # Field name made lowercase.
    benloccodsig = models.SmallIntegerField(db_column='BenLocCodSig', blank=True, null=True)  # Field name made lowercase.
    benbarcod = models.ForeignKey(Barrios, models.DO_NOTHING, db_column='BenBarCod', blank=True, null=True)  # Field name made lowercase.
    bendomcod = models.ForeignKey(Calle, models.DO_NOTHING, db_column='BenDomCod', blank=True, null=True)  # Field name made lowercase.
    benasigtipoopcional = models.SmallIntegerField(db_column='BenAsigTipoOpcional', blank=True, null=True)  # Field name made lowercase.
    bennrolote = models.CharField(db_column='BenNroLote', max_length=10, blank=True, null=True)  # Field name made lowercase.
    bennroparcela = models.CharField(db_column='BenNroParcela', max_length=10, blank=True, null=True)  # Field name made lowercase.
    bennromacizo = models.CharField(db_column='BenNroMacizo', max_length=10, blank=True, null=True)  # Field name made lowercase.
    bennromzana = models.CharField(db_column='BenNroMzana', max_length=10, blank=True, null=True)  # Field name made lowercase.
    bennrocasa = models.CharField(db_column='BenNroCasa', max_length=10, blank=True, null=True)  # Field name made lowercase.
    benprghgr = models.CharField(db_column='BenPrgHgr', max_length=2, blank=True, null=True)  # Field name made lowercase.
    benresfch = models.DateTimeField(db_column='BenResFch', blank=True, null=True)  # Field name made lowercase.
    bentipdoc = models.CharField(db_column='BenTipDoc', max_length=20, blank=True, null=True)  # Field name made lowercase.
    benasigtipog10 = models.BooleanField(db_column='BenAsigTipoG10', blank=True, null=True)  # Field name made lowercase.
    benasigtipog15 = models.BooleanField(db_column='BenAsigTipoG15', blank=True, null=True)  # Field name made lowercase.
    benasigtipot30 = models.BooleanField(db_column='BenAsigTipoT30', blank=True, null=True)  # Field name made lowercase.
    benasigtipot45 = models.BooleanField(db_column='BenAsigTipoT45', blank=True, null=True)  # Field name made lowercase.
    benasigtipogr90 = models.BooleanField(db_column='BenAsigTipoGr90', blank=True, null=True)  # Field name made lowercase.
    benciuid = models.ForeignKey(Ciudades, models.DO_NOTHING, db_column='BenCiuId', blank=True, null=True)  # Field name made lowercase.
    benciubarcod = models.SmallIntegerField(db_column='BenCiuBarCod', blank=True, null=True)  # Field name made lowercase.
    benciubardes = models.CharField(db_column='BenCiuBarDes', max_length=80, blank=True, null=True)  # Field name made lowercase.
    benape = models.CharField(db_column='BenApe', max_length=60, blank=True, null=True)  # Field name made lowercase.
    bennom = models.CharField(db_column='BenNom', max_length=60, blank=True, null=True)  # Field name made lowercase.
    benimportado = models.BooleanField(db_column='BenImportado', blank=True, null=True)  # Field name made lowercase.
    benimportadofecha = models.DateTimeField(db_column='BenImportadoFecha', blank=True, null=True)  # Field name made lowercase.
    benreempadronado = models.BooleanField(db_column='BenReempadronado')  # Field name made lowercase.
    benreempadronadofch = models.DateTimeField(db_column='BenReempadronadoFch', blank=True, null=True)  # Field name made lowercase.
    bencaracteristicafijo = models.CharField(db_column='BenCaracteristicaFijo', max_length=4)  # Field name made lowercase.
    bencaracterisiticacelular = models.CharField(db_column='BenCaracterisiticaCelular', max_length=4)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DjBenFam'


class Djbenfamdocumentos(models.Model):
    benid = models.OneToOneField(Djbenfam, models.DO_NOTHING, db_column='BenId', primary_key=True)  # Field name made lowercase.
    bendoccod = models.ForeignKey('Rdocumet', models.DO_NOTHING, db_column='BenDocCod')  # Field name made lowercase.
    bendocprefch = models.DateTimeField(db_column='BenDocPreFch', blank=True, null=True)  # Field name made lowercase.
    bendocpre = models.BooleanField(db_column='BenDocPre', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DjBenFamDocumentos'
        unique_together = (('benid', 'bendoccod'),)


class Djbenfamfamiliares(models.Model):
    benid = models.IntegerField(db_column='BenId', primary_key=True)  # Field name made lowercase.
    benfamnrodoc = models.IntegerField(db_column='BenFamNroDoc')  # Field name made lowercase.
    benfamnomape = models.CharField(db_column='BenFamNomApe', max_length=60, blank=True, null=True)  # Field name made lowercase.
    benfamtipo = models.ForeignKey('Rparent', models.DO_NOTHING, db_column='BenFamTipo', blank=True, null=True)  # Field name made lowercase.
    benfamedad = models.SmallIntegerField(db_column='BenFamEdad', blank=True, null=True)  # Field name made lowercase.
    benfamcivest = models.ForeignKey('Restciv', models.DO_NOTHING, db_column='BenFamCivEst', blank=True, null=True)  # Field name made lowercase.
    benfamnaccod = models.ForeignKey('Rpais', models.DO_NOTHING, db_column='BenFamNacCod', blank=True, null=True)  # Field name made lowercase.
    benfamocu = models.CharField(db_column='BenFamOcu', max_length=40, blank=True, null=True)  # Field name made lowercase.
    benfamsexo = models.SmallIntegerField(db_column='BenFamSexo', blank=True, null=True)  # Field name made lowercase.
    benfamnrocuit = models.DecimalField(db_column='BenFamNroCUIT', max_digits=11, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    benfamnom = models.CharField(db_column='BenFamNom', max_length=60, blank=True, null=True)  # Field name made lowercase.
    benfamape = models.CharField(db_column='BenFamApe', max_length=60, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DjBenFamFamiliares'
        unique_together = (('benid', 'benfamnrodoc'),)


class Entorno(models.Model):
    entorno = models.CharField(db_column='Entorno', primary_key=True, max_length=40)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Entorno'


class Excesocub(models.Model):
    excesocubid = models.AutoField(db_column='ExcesoCubId', primary_key=True)  # Field name made lowercase.
    excesocublocalidad = models.CharField(db_column='ExcesoCubLocalidad', max_length=20)  # Field name made lowercase.
    excesocubdom = models.CharField(db_column='ExcesoCubDom', max_length=150, blank=True, null=True)  # Field name made lowercase.
    excesocubfchtrn = models.DateTimeField(db_column='ExcesoCubFchTrn', blank=True, null=True)  # Field name made lowercase.
    excesocubhratrn = models.CharField(db_column='ExcesoCubHraTrn', max_length=20, blank=True, null=True)  # Field name made lowercase.
    excesocubtrngobid = models.IntegerField(db_column='ExcesoCubTrnGobId', blank=True, null=True)  # Field name made lowercase.
    excesocubdni = models.IntegerField(db_column='ExcesoCubDNI', blank=True, null=True)  # Field name made lowercase.
    excesocubapenom = models.CharField(db_column='ExcesoCubApeNom', max_length=40, blank=True, null=True)  # Field name made lowercase.
    excesocubperdes = models.DateTimeField(db_column='ExcesoCubPerDes', blank=True, null=True)  # Field name made lowercase.
    excesocubenvtip = models.SmallIntegerField(db_column='ExcesoCubEnvTip', blank=True, null=True)  # Field name made lowercase.
    excesocubcntdes = models.IntegerField(db_column='ExcesoCubCntDes', blank=True, null=True)  # Field name made lowercase.
    excesocubcomercio = models.CharField(db_column='ExcesoCubComercio', max_length=20, blank=True, null=True)  # Field name made lowercase.
    excesocubletctr = models.CharField(db_column='ExcesoCubLetCtr', max_length=20, blank=True, null=True)  # Field name made lowercase.
    excesocubtipope = models.CharField(db_column='ExcesoCubTipOpe', max_length=20, blank=True, null=True)  # Field name made lowercase.
    excesocubanu = models.CharField(db_column='ExcesoCubAnu', max_length=2, blank=True, null=True)  # Field name made lowercase.
    excesocubhash = models.CharField(db_column='ExcesoCubHash', max_length=32, blank=True, null=True)  # Field name made lowercase.
    excesocubkgasignado = models.SmallIntegerField(db_column='ExcesoCubKgAsignado', blank=True, null=True)  # Field name made lowercase.
    excesocubkgexcedido = models.SmallIntegerField(db_column='ExcesoCubKgExcedido', blank=True, null=True)  # Field name made lowercase.
    excesocubusrimp = models.CharField(db_column='ExcesoCubUsrImp', max_length=20, blank=True, null=True)  # Field name made lowercase.
    excesocubrectificado = models.BooleanField(db_column='ExcesoCubRectificado', blank=True, null=True)  # Field name made lowercase.
    excesocubrectiffecha = models.DateTimeField(db_column='ExcesoCubRectifFecha', blank=True, null=True)  # Field name made lowercase.
    excesocubusrrectificador = models.CharField(db_column='ExcesoCubUsrRectificador', max_length=20, blank=True, null=True)  # Field name made lowercase.
    excesocubfchimp = models.DateTimeField(db_column='ExcesoCubFchImp', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ExcesoCub'


class Excesotar(models.Model):
    excesotarid = models.AutoField(db_column='ExcesoTarId', primary_key=True)  # Field name made lowercase.
    excesotarcomid = models.IntegerField(db_column='ExcesoTarComId')  # Field name made lowercase.
    excesotarcodprod = models.IntegerField(db_column='ExcesoTarCodProd')  # Field name made lowercase.
    excesotarfchtrn = models.DateTimeField(db_column='ExcesoTarFchTrn')  # Field name made lowercase.
    excesotarhratrn = models.CharField(db_column='ExcesoTarHraTrn', max_length=20)  # Field name made lowercase.
    excesotarterid = models.CharField(db_column='ExcesoTarTerId', max_length=20)  # Field name made lowercase.
    excesotarcodaut = models.CharField(db_column='ExcesoTarCodAut', max_length=20)  # Field name made lowercase.
    excesotarlot = models.CharField(db_column='ExcesoTarLot', max_length=20)  # Field name made lowercase.
    excesotarcntenv = models.SmallIntegerField(db_column='ExcesoTarCntEnv')  # Field name made lowercase.
    excesotarcntdes = models.IntegerField(db_column='ExcesoTarCntDes')  # Field name made lowercase.
    excesotaranu = models.CharField(db_column='ExcesoTarAnu', max_length=2)  # Field name made lowercase.
    excesotartip = models.CharField(db_column='ExcesoTarTip', max_length=20)  # Field name made lowercase.
    excesotarnrotar = models.CharField(db_column='ExcesoTarNroTar', max_length=20)  # Field name made lowercase.
    excesotarapenom = models.CharField(db_column='ExcesoTarApeNom', max_length=40)  # Field name made lowercase.
    excesotardni = models.IntegerField(db_column='ExcesoTarDNI')  # Field name made lowercase.
    excesotarlocalidad = models.CharField(db_column='ExcesoTarLocalidad', max_length=20)  # Field name made lowercase.
    excesotardom = models.CharField(db_column='ExcesoTarDom', max_length=150)  # Field name made lowercase.
    excesotartrngobid = models.IntegerField(db_column='ExcesoTarTrnGobId')  # Field name made lowercase.
    excesotarfchimp = models.DateTimeField(db_column='ExcesoTarFchImp')  # Field name made lowercase.
    excesotarkgasignado = models.SmallIntegerField(db_column='ExcesoTarKgAsignado')  # Field name made lowercase.
    excesotarkgexcedido = models.SmallIntegerField(db_column='ExcesoTarKgExcedido')  # Field name made lowercase.
    excesotarhash = models.CharField(db_column='ExcesoTarHash', max_length=32)  # Field name made lowercase.
    excesotarusrimp = models.CharField(db_column='ExcesoTarUsrImp', max_length=20)  # Field name made lowercase.
    excesotarrectificado = models.BooleanField(db_column='ExcesoTarRectificado')  # Field name made lowercase.
    excesotarfecharectificacion = models.DateTimeField(db_column='ExcesoTarFechaRectificacion')  # Field name made lowercase.
    excesotarusuariorectificador = models.CharField(db_column='ExcesoTarUsuarioRectificador', max_length=20)  # Field name made lowercase.
    excesotarnrocup = models.CharField(db_column='ExcesoTarNroCup', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ExcesoTar'


class Mantenimiento(models.Model):
    mantenimiento = models.BooleanField(db_column='Mantenimiento', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Mantenimiento'


class Menuprincipal(models.Model):
    menuid = models.AutoField(db_column='MenuID', primary_key=True)  # Field name made lowercase.
    menutitulo = models.CharField(db_column='MenuTitulo', max_length=40)  # Field name made lowercase.
    menudescripcion = models.CharField(db_column='MenuDescripcion', max_length=80)  # Field name made lowercase.
    menuurl = models.CharField(db_column='MenuURL', max_length=1000)  # Field name made lowercase.
    menuparentid = models.ForeignKey('self', models.DO_NOTHING, db_column='MenuParentID', blank=True, null=True)  # Field name made lowercase.
    menuorden = models.SmallIntegerField(db_column='MenuOrden')  # Field name made lowercase.
    menuusuariocreador = models.CharField(db_column='MenuUsuarioCreador', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MenuPrincipal'


class Operaciontipo(models.Model):
    operaciontipoid = models.AutoField(db_column='OperacionTipoId', primary_key=True)  # Field name made lowercase.
    operaciontipodescripcion = models.CharField(db_column='OperacionTipoDescripcion', max_length=40)  # Field name made lowercase.
    operaciontipofechacreacion = models.DateTimeField(db_column='OperacionTipoFechaCreacion')  # Field name made lowercase.
    operaciontipovigente = models.BooleanField(db_column='OperacionTipoVigente')  # Field name made lowercase.
    operaciontipofechabaja = models.DateTimeField(db_column='OperacionTipoFechaBaja', blank=True, null=True)  # Field name made lowercase.
    operaciontipousuariocreador = models.CharField(db_column='OperacionTipoUsuarioCreador', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OperacionTipo'


class Operacionusuario(models.Model):
    operacionusuarioid = models.AutoField(db_column='OperacionUsuarioId', primary_key=True)  # Field name made lowercase.
    operacionusuariodni = models.IntegerField(db_column='OperacionUsuarioDNI')  # Field name made lowercase.
    operaciontipoid = models.ForeignKey(Operaciontipo, models.DO_NOTHING, db_column='OperacionTipoId')  # Field name made lowercase.
    operacionusuariofecha = models.DateTimeField(db_column='OperacionUsuarioFecha')  # Field name made lowercase.
    operacionusuariousuariosistema = models.CharField(db_column='OperacionUsuarioUsuarioSistema', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OperacionUsuario'


class Padben(models.Model):
    padbennrodoc = models.IntegerField(db_column='PadBenNroDoc', primary_key=True)  # Field name made lowercase.
    padbencuit = models.DecimalField(db_column='PadBenCuit', max_digits=11, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    padbennomape = models.CharField(db_column='PadBenNomApe', max_length=60, blank=True, null=True)  # Field name made lowercase.
    padbenlugnac = models.CharField(db_column='PadBenLugNac', max_length=40, blank=True, null=True)  # Field name made lowercase.
    padbennac = models.ForeignKey('Rpais', models.DO_NOTHING, db_column='PadBenNac', blank=True, null=True)  # Field name made lowercase.
    padbensexo = models.SmallIntegerField(db_column='PadBenSexo', blank=True, null=True)  # Field name made lowercase.
    padbenfecnac = models.DateTimeField(db_column='PadBenFecNac', blank=True, null=True)  # Field name made lowercase.
    padbencivest = models.ForeignKey('Restciv', models.DO_NOTHING, db_column='PadBenCivEst', blank=True, null=True)  # Field name made lowercase.
    padbenrectmp = models.SmallIntegerField(db_column='PadBenRecTmp', blank=True, null=True)  # Field name made lowercase.
    padbenrectmpmed = models.SmallIntegerField(db_column='PadBenRecTmpMed', blank=True, null=True)  # Field name made lowercase.
    padbenloc = models.CharField(db_column='PadBenLoc', max_length=20, blank=True, null=True)  # Field name made lowercase.
    padbenbarcod = models.ForeignKey(Barrios, models.DO_NOTHING, db_column='PadBenBarCod', blank=True, null=True)  # Field name made lowercase.
    padbenbarrio = models.CharField(db_column='PadBenBarrio', max_length=40, blank=True, null=True)  # Field name made lowercase.
    padbencalcodsig = models.ForeignKey(Calle, models.DO_NOTHING, db_column='PadBenCalCodSig', blank=True, null=True)  # Field name made lowercase.
    padbenzona = models.CharField(db_column='PadBenZona', max_length=20, blank=True, null=True)  # Field name made lowercase.
    padbendomcal = models.CharField(db_column='PadBenDomCal', max_length=40, blank=True, null=True)  # Field name made lowercase.
    padbendomnro = models.SmallIntegerField(db_column='PadBenDomNro', blank=True, null=True)  # Field name made lowercase.
    padbentel = models.CharField(db_column='PadBenTel', max_length=20, blank=True, null=True)  # Field name made lowercase.
    padbencel = models.CharField(db_column='PadBenCel', max_length=20, blank=True, null=True)  # Field name made lowercase.
    padbening = models.DecimalField(db_column='PadBenIng', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    padbenemail = models.CharField(db_column='PadBenEMail', max_length=100, blank=True, null=True)  # Field name made lowercase.
    padbenasigtipo = models.SmallIntegerField(db_column='PadBenAsigTipo', blank=True, null=True)  # Field name made lowercase.
    padbenasigtipoopcional = models.SmallIntegerField(db_column='PadBenAsigTipoOpcional', blank=True, null=True)  # Field name made lowercase.
    padprghgr = models.CharField(db_column='PadPrgHgr', max_length=2, blank=True, null=True)  # Field name made lowercase.
    padbenobs = models.TextField(db_column='PadBenObs', blank=True, null=True)  # Field name made lowercase.
    padbenhash = models.CharField(db_column='PadBenHash', max_length=40, blank=True, null=True)  # Field name made lowercase.
    padbenfecbaja = models.DateTimeField(db_column='PadBenFecBaja', blank=True, null=True)  # Field name made lowercase.
    padbenfecact = models.DateTimeField(db_column='PadBenFecAct', blank=True, null=True)  # Field name made lowercase.
    padbenusract = models.CharField(db_column='PadBenUsrAct', max_length=20, blank=True, null=True)  # Field name made lowercase.
    padbenfecalt = models.DateTimeField(db_column='PadBenFecAlt', blank=True, null=True)  # Field name made lowercase.
    padbenmod = models.BooleanField(db_column='PadBenMod', blank=True, null=True)  # Field name made lowercase.
    padbentipdoc = models.CharField(db_column='PadBenTipDoc', max_length=20, blank=True, null=True)  # Field name made lowercase.
    padbenresfch = models.DateTimeField(db_column='PadBenResFch', blank=True, null=True)  # Field name made lowercase.
    padbenasigtipog10 = models.BooleanField(db_column='PadBenAsigTipoG10', blank=True, null=True)  # Field name made lowercase.
    padbenasigtipog15 = models.BooleanField(db_column='PadBenAsigTipoG15', blank=True, null=True)  # Field name made lowercase.
    padbenasigtipot30 = models.BooleanField(db_column='PadBenAsigTipoT30', blank=True, null=True)  # Field name made lowercase.
    padbenasigtipot45 = models.BooleanField(db_column='PadBenAsigTipoT45', blank=True, null=True)  # Field name made lowercase.
    padbenasigtipogr90 = models.BooleanField(db_column='PadBenAsigTipoGr90', blank=True, null=True)  # Field name made lowercase.
    padbenrazbaja = models.TextField(db_column='PadBenRazBaja', blank=True, null=True)  # Field name made lowercase.
    padbenape = models.CharField(db_column='PadBenApe', max_length=60, blank=True, null=True)  # Field name made lowercase.
    padbennom = models.CharField(db_column='PadBenNom', max_length=60, blank=True, null=True)  # Field name made lowercase.
    padbennrocasa = models.CharField(db_column='PadBenNroCasa', max_length=10, blank=True, null=True)  # Field name made lowercase.
    padbennrolote = models.CharField(db_column='PadBenNroLote', max_length=10, blank=True, null=True)  # Field name made lowercase.
    padbennroparcela = models.CharField(db_column='PadBenNroParcela', max_length=10, blank=True, null=True)  # Field name made lowercase.
    padbennromacizo = models.CharField(db_column='PadbenNroMacizo', max_length=10, blank=True, null=True)  # Field name made lowercase.
    padbennromanzana = models.CharField(db_column='PadBenNroManzana', max_length=10, blank=True, null=True)  # Field name made lowercase.
    padbendesbaj = models.CharField(db_column='PadBenDesBaj', max_length=80, blank=True, null=True)  # Field name made lowercase.
    padbenimportado = models.BooleanField(db_column='PadBenImportado', blank=True, null=True)  # Field name made lowercase.
    padbenimportadofecha = models.DateTimeField(db_column='PadBenImportadoFecha', blank=True, null=True)  # Field name made lowercase.
    padbenreempadronado = models.BooleanField(db_column='PadBenReempadronado')  # Field name made lowercase.
    padbentipbajid = models.ForeignKey('Tipobaja', models.DO_NOTHING, db_column='PadBenTipBajId', blank=True, null=True)  # Field name made lowercase.
    padbenreempadronadofecha = models.DateTimeField(db_column='PadBenReempadronadoFecha', blank=True, null=True)  # Field name made lowercase.
    padbencaracteristicafijo = models.CharField(db_column='PadBenCaracteristicaFijo', max_length=4, blank=True, null=True)  # Field name made lowercase.
    padbencaracteristicacelular = models.CharField(db_column='PadBenCaracteristicaCelular', max_length=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PadBen'


class Padbendocumentos(models.Model):
    padbennrodoc = models.OneToOneField(Padben, models.DO_NOTHING, db_column='PadBenNroDoc', primary_key=True)  # Field name made lowercase.
    padbendoccod = models.ForeignKey('Rdocumet', models.DO_NOTHING, db_column='PadBenDocCod')  # Field name made lowercase.
    padbendocprefch = models.DateTimeField(db_column='PadBenDocPreFch', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PadBenDocumentos'
        unique_together = (('padbennrodoc', 'padbendoccod'),)


class Padbenfamiliares(models.Model):
    padbennrodoc = models.IntegerField(db_column='PadBenNroDoc', primary_key=True)  # Field name made lowercase.
    padbenfamnrodoc = models.IntegerField(db_column='PadBenFamNroDoc')  # Field name made lowercase.
    padbenfamnomape = models.CharField(db_column='PadBenFamNomApe', max_length=60, blank=True, null=True)  # Field name made lowercase.
    padbenfamsexo = models.SmallIntegerField(db_column='PadBenFamSexo', blank=True, null=True)  # Field name made lowercase.
    padbenfamtipo = models.ForeignKey('Rparent', models.DO_NOTHING, db_column='PadBenFamTipo', blank=True, null=True)  # Field name made lowercase.
    padbenfamedad = models.SmallIntegerField(db_column='PadBenFamEdad', blank=True, null=True)  # Field name made lowercase.
    padbenfamcivest = models.ForeignKey('Restciv', models.DO_NOTHING, db_column='PadBenFamCivEst', blank=True, null=True)  # Field name made lowercase.
    padbenfamnaccod = models.ForeignKey('Rpais', models.DO_NOTHING, db_column='PadBenFamNacCod', blank=True, null=True)  # Field name made lowercase.
    padbenfamocu = models.CharField(db_column='PadBenFamOcu', max_length=20, blank=True, null=True)  # Field name made lowercase.
    padbennrocuit = models.DecimalField(db_column='PadBenNroCUIT', max_digits=11, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    padbenfamnom = models.CharField(db_column='PadBenFamNom', max_length=60, blank=True, null=True)  # Field name made lowercase.
    padbenfamape = models.CharField(db_column='PadBenFamApe', max_length=60, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PadBenFamiliares'
        unique_together = (('padbennrodoc', 'padbenfamnrodoc'),)


class Padbenhistorico(models.Model):
    padbenhisid = models.AutoField(db_column='PadBenHisId', primary_key=True)  # Field name made lowercase.
    padbenhisnrodoc = models.IntegerField(db_column='PadBenHisNroDoc', blank=True, null=True)  # Field name made lowercase.
    padbenhiscuit = models.SmallIntegerField(db_column='PadBenHisCuit', blank=True, null=True)  # Field name made lowercase.
    padbenhistipdoc = models.CharField(db_column='PadBenHisTipDoc', max_length=1, blank=True, null=True)  # Field name made lowercase.
    padbenhisape = models.CharField(db_column='PadBenHisApe', max_length=25, blank=True, null=True)  # Field name made lowercase.
    padbenhisnom = models.CharField(db_column='PadBenHisNom', max_length=25, blank=True, null=True)  # Field name made lowercase.
    padbenhislugnac = models.CharField(db_column='PadBenHisLugNac', max_length=20, blank=True, null=True)  # Field name made lowercase.
    padbenhisnac = models.CharField(db_column='PadBenHisNac', max_length=20, blank=True, null=True)  # Field name made lowercase.
    padbenhissexo = models.CharField(db_column='PadBenHisSexo', max_length=9, blank=True, null=True)  # Field name made lowercase.
    padbenhisfecnac = models.DateTimeField(db_column='PadBenHisFecNac', blank=True, null=True)  # Field name made lowercase.
    padbenhiscivest = models.CharField(db_column='PadBenHisCivEst', max_length=20, blank=True, null=True)  # Field name made lowercase.
    padbenhisfchingisl = models.DateTimeField(db_column='PadBenHisFchIngIsl', blank=True, null=True)  # Field name made lowercase.
    padbenhisloc = models.CharField(db_column='PadBenHisLoc', max_length=20, blank=True, null=True)  # Field name made lowercase.
    padbenhisbardes = models.CharField(db_column='PadBenHisBarDes', max_length=30, blank=True, null=True)  # Field name made lowercase.
    padbenhiscalnom = models.CharField(db_column='PadBenHisCalNom', max_length=40, blank=True, null=True)  # Field name made lowercase.
    padbenhiscalnro = models.SmallIntegerField(db_column='PadBenHisCalNro', blank=True, null=True)  # Field name made lowercase.
    padbenhisnrocasa = models.CharField(db_column='PadBenHisNroCasa', max_length=20, blank=True, null=True)  # Field name made lowercase.
    padbenhisnrolote = models.CharField(db_column='PadBenHisNroLote', max_length=20, blank=True, null=True)  # Field name made lowercase.
    padbenhisnroparcela = models.CharField(db_column='PadBenHisNroParcela', max_length=20, blank=True, null=True)  # Field name made lowercase.
    padbenhisnromacizo = models.CharField(db_column='PadbenHisNroMacizo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    padbenhisnromanzana = models.CharField(db_column='PadBenHisNroManzana', max_length=20, blank=True, null=True)  # Field name made lowercase.
    padbenhiszona = models.CharField(db_column='PadBenHisZona', max_length=20, blank=True, null=True)  # Field name made lowercase.
    padbenhistel = models.CharField(db_column='PadBenHisTel', max_length=20, blank=True, null=True)  # Field name made lowercase.
    padbenhiscel = models.CharField(db_column='PadBenHisCel', max_length=20, blank=True, null=True)  # Field name made lowercase.
    padbenhisemail = models.CharField(db_column='PadBenHisEMail', max_length=100, blank=True, null=True)  # Field name made lowercase.
    padbenhisobs = models.CharField(db_column='PadBenHisObs', max_length=200, blank=True, null=True)  # Field name made lowercase.
    padbenhisfecalt = models.DateTimeField(db_column='PadBenHisFecAlt', blank=True, null=True)  # Field name made lowercase.
    padbenhisfecbaja = models.DateTimeField(db_column='PadBenHisFecBaja', blank=True, null=True)  # Field name made lowercase.
    padbenhisdesbaj = models.CharField(db_column='PadBenHisDesBaj', max_length=40, blank=True, null=True)  # Field name made lowercase.
    padbenhisrazbaja = models.CharField(db_column='PadBenHisRazBaja', max_length=100, blank=True, null=True)  # Field name made lowercase.
    padbenhisusrbaja = models.CharField(db_column='PadBenHisUsrBaja', max_length=20, blank=True, null=True)  # Field name made lowercase.
    padbenhisfecact = models.DateTimeField(db_column='PadBenHisFecAct', blank=True, null=True)  # Field name made lowercase.
    padbenhisusract = models.CharField(db_column='PadBenHisUsrAct', max_length=20, blank=True, null=True)  # Field name made lowercase.
    padbenhisasigtipog10 = models.BooleanField(db_column='PadBenHisAsigTipoG10', blank=True, null=True)  # Field name made lowercase.
    padbehisnasigtipog15 = models.BooleanField(db_column='PadBeHisnAsigTipoG15', blank=True, null=True)  # Field name made lowercase.
    padbenhisasigtipot30 = models.BooleanField(db_column='PadBenHisAsigTipoT30', blank=True, null=True)  # Field name made lowercase.
    padbenhisasigtipot45 = models.BooleanField(db_column='PadBenHisAsigTipoT45', blank=True, null=True)  # Field name made lowercase.
    padbenhisasigtipogr90 = models.BooleanField(db_column='PadBenHisAsigTipoGr90', blank=True, null=True)  # Field name made lowercase.
    padbenhisimportado = models.BooleanField(db_column='PadBenHisImportado', blank=True, null=True)  # Field name made lowercase.
    padbenhisimportadofecha = models.DateTimeField(db_column='PadBenHisImportadoFecha', blank=True, null=True)  # Field name made lowercase.
    padbenhisreempadronado = models.BooleanField(db_column='PadBenHisReempadronado', blank=True, null=True)  # Field name made lowercase.
    padbenhisaccion = models.CharField(db_column='PadBenHisAccion', max_length=80)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PadBenHistorico'


class Perfiles(models.Model):
    perfilesid = models.IntegerField(db_column='PerfilesID', primary_key=True)  # Field name made lowercase.
    perfilesdescripcion = models.CharField(db_column='PerfilesDescripcion', max_length=40)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Perfiles'


class Perfilespermisos(models.Model):
    perfilesid = models.OneToOneField(Perfiles, models.DO_NOTHING, db_column='PerfilesID', primary_key=True)  # Field name made lowercase.
    webobjetosid = models.ForeignKey('Webobjetos', models.DO_NOTHING, db_column='WebObjetosID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PerfilesPermisos'
        unique_together = (('perfilesid', 'webobjetosid'),)


class Periodoasignacion(models.Model):
    perasiid = models.AutoField(db_column='PerAsiId', primary_key=True)  # Field name made lowercase.
    perasides = models.CharField(db_column='PerAsiDes', max_length=9)  # Field name made lowercase.
    perasitopkg = models.SmallIntegerField(db_column='PerAsiTopKg')  # Field name made lowercase.
    perasifchini = models.DateTimeField(db_column='PerASiFchIni')  # Field name made lowercase.
    perasifchfin = models.DateTimeField(db_column='PerAsiFchFin')  # Field name made lowercase.
    perasiexekg = models.SmallIntegerField(db_column='PerAsiExeKg')  # Field name made lowercase.
    perasifchcreacion = models.DateTimeField(db_column='PerAsiFchCreacion')  # Field name made lowercase.
    perasiusrcreacion = models.CharField(db_column='PerAsiUsrCreacion', max_length=20)  # Field name made lowercase.
    perasivigente = models.BooleanField(db_column='PerAsiVigente')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PeriodoAsignacion'


class Pruebaimportacionws(models.Model):
    idimportacion = models.AutoField(db_column='Idimportacion', primary_key=True)  # Field name made lowercase.
    anulado = models.CharField(db_column='Anulado', max_length=2)  # Field name made lowercase.
    apellidonombre = models.CharField(db_column='ApellidoNombre', max_length=40)  # Field name made lowercase.
    cantidadkilos = models.SmallIntegerField(db_column='CantidadKilos')  # Field name made lowercase.
    ciudad = models.CharField(db_column='Ciudad', max_length=20)  # Field name made lowercase.
    codigoproveedor = models.CharField(db_column='CodigoProveedor', max_length=30)  # Field name made lowercase.
    fechatr = models.CharField(db_column='FechaTr', max_length=10)  # Field name made lowercase.
    horatr = models.CharField(db_column='HoraTr', max_length=10)  # Field name made lowercase.
    idcarga = models.IntegerField(db_column='IdCarga')  # Field name made lowercase.
    idtr = models.CharField(db_column='IdTr', max_length=20)  # Field name made lowercase.
    nrodoc = models.CharField(db_column='NroDoc', max_length=8)  # Field name made lowercase.
    periodo = models.CharField(db_column='Periodo', max_length=10)  # Field name made lowercase.
    prodid = models.CharField(db_column='ProdId', max_length=20)  # Field name made lowercase.
    tipotrans = models.CharField(db_column='TipoTrans', max_length=20)  # Field name made lowercase.
    ubicacionentrega = models.CharField(db_column='UbicacionEntrega', max_length=20)  # Field name made lowercase.
    barrio = models.CharField(db_column='Barrio', max_length=40)  # Field name made lowercase.
    fechaimportacion = models.DateTimeField(db_column='FechaImportacion')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PruebaImportacionWS'


class Solusrben(models.Model):
    solusrbenid = models.AutoField(db_column='SolUsrBenid', primary_key=True)  # Field name made lowercase.
    solusrbencuit = models.DecimalField(db_column='SolUsrBenCuit', max_digits=11, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    solusrbennrodoc = models.IntegerField(db_column='SolUsrBenNroDoc')  # Field name made lowercase.
    solusrbensexo = models.SmallIntegerField(db_column='SolUsrBenSexo')  # Field name made lowercase.
    solusrbennomape = models.CharField(db_column='SolUsrBenNomApe', max_length=60)  # Field name made lowercase.
    solusrbenemail = models.CharField(db_column='SolUsrBenEMail', max_length=100, blank=True, null=True)  # Field name made lowercase.
    solusrbenrealizado = models.BooleanField(db_column='SolUsrBenRealizado', blank=True, null=True)  # Field name made lowercase.
    solusrbenfecharealizado = models.DateTimeField(db_column='SolUsrBenFechaRealizado', blank=True, null=True)  # Field name made lowercase.
    solusrbenusuariorealizo = models.CharField(db_column='SolUsrBenUsuarioRealizo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    solusrbenfechasolicitud = models.DateTimeField(db_column='SolUsrBenFechaSolicitud')  # Field name made lowercase.
    solusrbenrechazado = models.BooleanField(db_column='SolUsrBenRechazado', blank=True, null=True)  # Field name made lowercase.
    solusrbenmsgrechazo = models.TextField(db_column='SolUsrBenMsgRechazo', blank=True, null=True)  # Field name made lowercase.
    solusrbentelcia = models.CharField(db_column='SolUsrBenTelCia', max_length=10, blank=True, null=True)  # Field name made lowercase.
    solusrbentelcontacto = models.CharField(db_column='SolUsrBenTelContacto', max_length=20, blank=True, null=True)  # Field name made lowercase.
    solusrbennoemail = models.BooleanField(db_column='SolUsrBenNoEmail', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SolUsrBen'


class Tmpcubo(models.Model):
    tmpcuboid = models.AutoField(db_column='TMPCuboId', primary_key=True)  # Field name made lowercase.
    tmpcuboloc = models.CharField(db_column='TMPCuboLoc', max_length=20, blank=True, null=True)  # Field name made lowercase.
    tmpcubodom = models.CharField(db_column='TMPCuboDom', max_length=150, blank=True, null=True)  # Field name made lowercase.
    tmpcubofchtrn = models.DateTimeField(db_column='TMPCuboFchTrn', blank=True, null=True)  # Field name made lowercase.
    tmpcubohratrn = models.CharField(db_column='TMPCuboHraTrn', max_length=20, blank=True, null=True)  # Field name made lowercase.
    tmpcuboidtrngob = models.IntegerField(db_column='TMPCuboIdTrnGob', blank=True, null=True)  # Field name made lowercase.
    tmpcubodni = models.IntegerField(db_column='TMPCuboDni', blank=True, null=True)  # Field name made lowercase.
    tmpcuboapenom = models.CharField(db_column='TMPCuboApeNom', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tmpcuboperdes = models.DateTimeField(db_column='TMPCuboPerDes', blank=True, null=True)  # Field name made lowercase.
    tmpcuboenvtip = models.SmallIntegerField(db_column='TMPCuboEnvTip', blank=True, null=True)  # Field name made lowercase.
    tmpcubocandes = models.DecimalField(db_column='TMPCuboCanDes', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tmpcubocomercio = models.CharField(db_column='TMPCuboComercio', max_length=20, blank=True, null=True)  # Field name made lowercase.
    tmpcuboletctr = models.CharField(db_column='TMPCuboLetCtr', max_length=2, blank=True, null=True)  # Field name made lowercase.
    tmpcubotipope = models.CharField(db_column='TMPCuboTipOpe', max_length=20, blank=True, null=True)  # Field name made lowercase.
    tmpcubofchimp = models.DateTimeField(db_column='TMPCuboFchImp', blank=True, null=True)  # Field name made lowercase.
    tmpcubohash = models.CharField(db_column='TMPCuboHash', max_length=32, blank=True, null=True)  # Field name made lowercase.
    tmpcuboanu = models.CharField(db_column='TMPCuboAnu', max_length=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TMPCubo'


class Tmpsistema(models.Model):
    tmpsistemaid = models.AutoField(db_column='TMPSistemaId', primary_key=True)  # Field name made lowercase.
    tmpsistemaidcom = models.IntegerField(db_column='TMPSistemaIdCom', blank=True, null=True)  # Field name made lowercase.
    tmpsistemacomercio = models.CharField(db_column='TMPSistemaComercio', max_length=20, blank=True, null=True)  # Field name made lowercase.
    tmpsistemacodprod = models.DecimalField(db_column='TMPSistemaCodProd', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tmpsistemafchtrn = models.DateTimeField(db_column='TMPSistemaFchTrn', blank=True, null=True)  # Field name made lowercase.
    tmpsistemahratrn = models.CharField(db_column='TMPSistemaHraTrn', max_length=20, blank=True, null=True)  # Field name made lowercase.
    tmpsistemaidter = models.CharField(db_column='TMPSistemaIdTer', max_length=20, blank=True, null=True)  # Field name made lowercase.
    tmpsistemacodaut = models.CharField(db_column='TMPSistemaCodAut', max_length=20, blank=True, null=True)  # Field name made lowercase.
    tmpsistemalot = models.CharField(db_column='TMPSistemaLot', max_length=20, blank=True, null=True)  # Field name made lowercase.
    tmpsistemanrocup = models.CharField(db_column='TMPSistemaNroCup', max_length=20, blank=True, null=True)  # Field name made lowercase.
    tmpsistemacntenv = models.SmallIntegerField(db_column='TMPSistemaCntEnv', blank=True, null=True)  # Field name made lowercase.
    tmpsistemaanu = models.CharField(db_column='TMPSistemaAnu', max_length=2, blank=True, null=True)  # Field name made lowercase.
    tmpsistematip = models.CharField(db_column='TMPSistemaTip', max_length=20, blank=True, null=True)  # Field name made lowercase.
    tmpsistemanrotar = models.CharField(db_column='TMPSistemaNroTar', max_length=20, blank=True, null=True)  # Field name made lowercase.
    tmpsistemaapenom = models.CharField(db_column='TMPSistemaApeNom', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tmpsistemadni = models.IntegerField(db_column='TMPSistemaDni', blank=True, null=True)  # Field name made lowercase.
    tmpsistemaloc = models.CharField(db_column='TMPSistemaLoc', max_length=20, blank=True, null=True)  # Field name made lowercase.
    tmpsistemadom = models.CharField(db_column='TMPSistemaDom', max_length=150, blank=True, null=True)  # Field name made lowercase.
    tmpsistemaidtrngob = models.IntegerField(db_column='TMPSistemaIdTrnGob', blank=True, null=True)  # Field name made lowercase.
    tmpsistemahash = models.CharField(db_column='TMPSistemaHash', max_length=32, blank=True, null=True)  # Field name made lowercase.
    tmpsistemacntdes = models.SmallIntegerField(db_column='TMPSistemaCntDes', blank=True, null=True)  # Field name made lowercase.
    tmpsistemafchimp = models.DateTimeField(db_column='TMPSistemaFchImp', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TMPSistema'


class Tarjetas(models.Model):
    tarjetasid = models.AutoField(db_column='TarjetasId', primary_key=True)  # Field name made lowercase.
    tarjetasdni = models.IntegerField(db_column='TarjetasDNI', blank=True, null=True)  # Field name made lowercase.
    tarjetasnro = models.CharField(db_column='TarjetasNro', max_length=20, blank=True, null=True)  # Field name made lowercase.
    tarjetasestado = models.CharField(db_column='TarjetasEstado', max_length=5, blank=True, null=True)  # Field name made lowercase.
    tarjetasvigentehasta = models.DateTimeField(db_column='TarjetasVigenteHasta', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tarjetas'


class Tipobaja(models.Model):
    tipbajid = models.IntegerField(db_column='TipBajId', primary_key=True)  # Field name made lowercase.
    tipbajdes = models.CharField(db_column='TipBajDes', max_length=80)  # Field name made lowercase.
    tipbajfchalt = models.DateTimeField(db_column='TipBajFchAlt')  # Field name made lowercase.
    tipbajfchbaj = models.DateTimeField(db_column='TipBajFchBaj')  # Field name made lowercase.
    tipbajexport = models.BooleanField(db_column='TipBajExport')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TipoBaja'


class Usrben(models.Model):
    usrbennrodoc = models.IntegerField(db_column='UsrBenNroDoc', primary_key=True)  # Field name made lowercase.
    usrbencuit = models.DecimalField(db_column='UsrBenCuit', max_digits=11, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    usrbensexo = models.SmallIntegerField(db_column='UsrBenSexo')  # Field name made lowercase.
    usrbennomape = models.CharField(db_column='UsrBenNomApe', max_length=60)  # Field name made lowercase.
    usrbenclave = models.CharField(db_column='UsrBenClave', max_length=20)  # Field name made lowercase.
    usrbenultacc = models.DateTimeField(db_column='UsrBenUltAcc', blank=True, null=True)  # Field name made lowercase.
    usrbenemail = models.CharField(db_column='UsrBenEmail', max_length=100)  # Field name made lowercase.
    usrbenfeccamcla = models.DateTimeField(db_column='UsrBenFecCamCla', blank=True, null=True)  # Field name made lowercase.
    usrbenccambioobligado = models.BooleanField(db_column='UsrBencCambioObligado', blank=True, null=True)  # Field name made lowercase.
    usrbenhashrecuperacion = models.CharField(db_column='UsrBenHashRecuperacion', max_length=40, blank=True, null=True)  # Field name made lowercase.
    usrbenfechahash = models.DateTimeField(db_column='UsrBenFechaHash', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'UsrBen'


class Usrprov(models.Model):
    usrprovcuit = models.DecimalField(db_column='UsrProvCUIT', primary_key=True, max_digits=11, decimal_places=0)  # Field name made lowercase.
    usrprovnombre = models.CharField(db_column='UsrProvNombre', max_length=40)  # Field name made lowercase.
    usrprovclave = models.CharField(db_column='UsrProvClave', max_length=64)  # Field name made lowercase.
    usrprovactivo = models.BooleanField(db_column='UsrProvActivo')  # Field name made lowercase.
    usrprovcomercio = models.CharField(db_column='UsrProvComercio', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'UsrProv'


class Usrprovmail(models.Model):
    usrprovcuit = models.OneToOneField(Usrprov, models.DO_NOTHING, db_column='UsrProvCUIT', primary_key=True)  # Field name made lowercase.
    usrprovmailid = models.IntegerField(db_column='UsrProvMailId')  # Field name made lowercase.
    usrprovmaildireccion = models.CharField(db_column='UsrProvMailDireccion', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'UsrProvMail'
        unique_together = (('usrprovcuit', 'usrprovmailid'),)


class Usuarios(models.Model):
    usrlogin = models.CharField(db_column='UsrLogin', primary_key=True, max_length=25)  # Field name made lowercase.
    usrnombre = models.CharField(db_column='UsrNombre', max_length=40)  # Field name made lowercase.
    usrapellido = models.CharField(db_column='UsrApellido', max_length=40)  # Field name made lowercase.
    usrdni = models.CharField(db_column='UsrDNI', max_length=20)  # Field name made lowercase.
    usradministrador = models.BooleanField(db_column='UsrAdministrador')  # Field name made lowercase.
    perfilesid = models.ForeignKey(Perfiles, models.DO_NOTHING, db_column='PerfilesID', blank=True, null=True)  # Field name made lowercase.
    usuariosnotificarmail = models.BooleanField(db_column='UsuariosNotificarMail')  # Field name made lowercase.
    usuariosloglevel = models.SmallIntegerField(db_column='UsuariosLogLevel')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Usuarios'


class Verificacub(models.Model):
    verificacubid = models.AutoField(db_column='VerificaCubId', primary_key=True)  # Field name made lowercase.
    verificacubloc = models.CharField(db_column='VerificaCubLoc', max_length=20, blank=True, null=True)  # Field name made lowercase.
    verificacubdom = models.CharField(db_column='VerificaCubDom', max_length=150, blank=True, null=True)  # Field name made lowercase.
    verificacubfchtrn = models.DateTimeField(db_column='VerificaCubFchTrn', blank=True, null=True)  # Field name made lowercase.
    verificacubhratrn = models.CharField(db_column='VerificaCubHraTrn', max_length=20, blank=True, null=True)  # Field name made lowercase.
    verificacubtrngobid = models.IntegerField(db_column='VerificaCubTrnGobId', blank=True, null=True)  # Field name made lowercase.
    verificacubdni = models.IntegerField(db_column='VerificaCubDNI', blank=True, null=True)  # Field name made lowercase.
    verificacubapenom = models.CharField(db_column='VerificaCubApeNom', max_length=40, blank=True, null=True)  # Field name made lowercase.
    verificacubperdes = models.DateTimeField(db_column='VerificaCubPerDes', blank=True, null=True)  # Field name made lowercase.
    verificacubenvtip = models.SmallIntegerField(db_column='VerificaCubEnvTip', blank=True, null=True)  # Field name made lowercase.
    verificacubcntdes = models.IntegerField(db_column='VerificaCubCntDes', blank=True, null=True)  # Field name made lowercase.
    verificacubcomercio = models.CharField(db_column='VerificaCubComercio', max_length=20, blank=True, null=True)  # Field name made lowercase.
    verificacubletctr = models.CharField(db_column='VerificaCubLetCtr', max_length=2, blank=True, null=True)  # Field name made lowercase.
    verificacubanu = models.CharField(db_column='VerificaCubAnu', max_length=2, blank=True, null=True)  # Field name made lowercase.
    verificacubfchimp = models.DateTimeField(db_column='VerificaCubFchImp', blank=True, null=True)  # Field name made lowercase.
    verificacubhash = models.CharField(db_column='VerificaCubHash', max_length=32, blank=True, null=True)  # Field name made lowercase.
    verificacubcntasignada = models.SmallIntegerField(db_column='VerificaCubCntAsignada', blank=True, null=True)  # Field name made lowercase.
    verificacubcntdescargada = models.SmallIntegerField(db_column='VerificaCubCntDescargada', blank=True, null=True)  # Field name made lowercase.
    verificacubcntexceso = models.SmallIntegerField(db_column='VerificaCubCntExceso', blank=True, null=True)  # Field name made lowercase.
    verificacubsaldo = models.SmallIntegerField(db_column='VerificaCubSaldo', blank=True, null=True)  # Field name made lowercase.
    verificacubtipope = models.CharField(db_column='VerificaCubTipOpe', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'VerificaCub'


class Verificatar(models.Model):
    verificatarid = models.AutoField(db_column='VerificaTarId', primary_key=True)  # Field name made lowercase.
    verificatarcomid = models.IntegerField(db_column='VerificaTarComId')  # Field name made lowercase.
    verificatarcomercio = models.CharField(db_column='VerificaTarComercio', max_length=20)  # Field name made lowercase.
    verificatarcodprod = models.IntegerField(db_column='VerificaTarCodProd')  # Field name made lowercase.
    verificatarfchtrn = models.DateTimeField(db_column='VerificaTarFchTrn')  # Field name made lowercase.
    verificatarhratrn = models.CharField(db_column='VerificaTarHraTrn', max_length=20)  # Field name made lowercase.
    verificatarterid = models.CharField(db_column='VerificaTarTerId', max_length=20)  # Field name made lowercase.
    verificatarcodaut = models.CharField(db_column='VerificaTarCodAut', max_length=20)  # Field name made lowercase.
    verificatarlot = models.CharField(db_column='VerificaTarLot', max_length=20)  # Field name made lowercase.
    verificatarnrocup = models.CharField(db_column='VerificaTarNroCup', max_length=20)  # Field name made lowercase.
    verificatarcntenv = models.SmallIntegerField(db_column='VerificaTarCntEnv')  # Field name made lowercase.
    verificatarcntdes = models.IntegerField(db_column='VerificaTarCntDes')  # Field name made lowercase.
    verificatarcntdessig = models.IntegerField(db_column='VerificaTarCntDesSig')  # Field name made lowercase.
    verificataranu = models.CharField(db_column='VerificaTarAnu', max_length=2)  # Field name made lowercase.
    verificatartip = models.CharField(db_column='VerificaTarTip', max_length=20)  # Field name made lowercase.
    verificatarnrotar = models.CharField(db_column='VerificaTarNroTar', max_length=20)  # Field name made lowercase.
    verificatarapenom = models.CharField(db_column='VerificaTarApeNom', max_length=40)  # Field name made lowercase.
    verificatardni = models.IntegerField(db_column='VerificaTarDNI')  # Field name made lowercase.
    verificatarloc = models.CharField(db_column='VerificaTarLoc', max_length=20)  # Field name made lowercase.
    verificatardom = models.CharField(db_column='VerificaTarDom', max_length=150)  # Field name made lowercase.
    verificatartrngobid = models.IntegerField(db_column='VerificaTarTrnGobId')  # Field name made lowercase.
    verificatarcntasignada = models.SmallIntegerField(db_column='VerificaTarCntAsignada')  # Field name made lowercase.
    verificatarcntdescargada = models.SmallIntegerField(db_column='VerificaTarCntDescargada')  # Field name made lowercase.
    verificatarcntexceso = models.SmallIntegerField(db_column='VerificaTarCntExceso')  # Field name made lowercase.
    verificatarsaldo = models.SmallIntegerField(db_column='VerificaTarSaldo')  # Field name made lowercase.
    verificatarhash = models.CharField(db_column='VerificaTarHash', max_length=32)  # Field name made lowercase.
    verificatarfchverifi = models.DateTimeField(db_column='VerificaTarFchVerifi')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'VerificaTar'

    def __str__(self):
        return '{}'.format(
            self.verificatarapenom,

        )


class Webobjetos(models.Model):
    webobjetosid = models.CharField(db_column='WebObjetosID', primary_key=True, max_length=40)  # Field name made lowercase.
    webobjetosdescripcion = models.CharField(db_column='WebObjetosDescripcion', max_length=60)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WebObjetos'


class Rdocumet(models.Model):
    rdoccod = models.SmallIntegerField(db_column='rDocCod', primary_key=True)  # Field name made lowercase.
    rdocdesc = models.CharField(db_column='rDocDesc', max_length=80)  # Field name made lowercase.
    rdocdiavto = models.SmallIntegerField(db_column='rDocDiaVto')  # Field name made lowercase.
    rdocper = models.BooleanField(db_column='rDocPer')  # Field name made lowercase.
    rdocvig = models.BooleanField(db_column='rDocVig')  # Field name made lowercase.
    rdocbaja = models.DateTimeField(db_column='rDocBaja', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'rDocumet'


class Restciv(models.Model):
    restcivcod = models.SmallIntegerField(primary_key=True)
    restcivdsc = models.CharField(max_length=40)
    restcivbaja = models.DateTimeField(db_column='rEstCivBaja', blank=True, null=True)  # Field name made lowercase.
    restcivcodsig = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'rEstCiv'


class Rpais(models.Model):
    rpaiscod = models.SmallIntegerField(db_column='rPaisCod', primary_key=True)  # Field name made lowercase.
    rpaisdsc = models.CharField(db_column='rPaisDsc', max_length=40)  # Field name made lowercase.
    rpaisbaja = models.DateTimeField(db_column='rPaisBaja', blank=True, null=True)  # Field name made lowercase.
    rpaiscodsig = models.SmallIntegerField(db_column='rPaisCodSig', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'rPais'


class Rparent(models.Model):
    rparentcod = models.SmallIntegerField(primary_key=True)
    rparentdsc = models.CharField(max_length=40)
    rparentbaja = models.DateTimeField(db_column='rParentBaja', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'rParent'


class Sysdiagrams(models.Model):
    name = models.CharField(max_length=128)
    principal_id = models.IntegerField()
    diagram_id = models.AutoField(primary_key=True)
    version = models.IntegerField(blank=True, null=True)
    definition = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sysdiagrams'
        unique_together = (('principal_id', 'name'),)
