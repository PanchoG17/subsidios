from django.contrib import admin

from apps.operaciones.models import Conimpcub, Verificacub, Verificatar

# Register your models here.
# admin.site.register(Conimpcub)

class VerificatarAdmin(admin.ModelAdmin):
    list_display=[
        'verificatarapenom',
        'verificatartip',
        'verificatarcntdes',

        'verificatarsaldo',
        'verificatarfchtrn',
    ]
    
    list_filter = [
        'verificatarapenom',
    ]

class VerificacubAdmin(admin.ModelAdmin):
    list_display = [
        'verificacubloc',
        'verificacubfchtrn',
        'verificacubapenom',
        'verificacubtipope',
        'verificacubenvtip',
        'verificacubcomercio',
        'verificacubsaldo',
        'verificacubcntasignada',
        'verificacubcntdescargada',
    ]
    list_filter =[
        'verificacubapenom',
        'verificacubtipope',
        'verificacubcomercio',
    ]

#admin.site.register(Verificacub, VerificacubAdmin)
#admin.site.register(Verificatar, VerificatarAdmin)