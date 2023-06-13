from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User, Group
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives

from core.services import ADWSLogin, ADWSGetUsuarioYPass, es_beneficiario, setToken
from apps.operaciones.models import Usuarios
from core.settings import EMAIL_HOST_USER
from email.mime.image import MIMEImage

from .forms import LoginAgenteForm, LoginBeneficiarioForm, SignUpAgenteForm, SignUpBeneficiarioForm

def login_home(request):
    return render(request, "accounts/login.html")

def login_beneficiarios(request):
    form = LoginBeneficiarioForm(request.POST or None)
    title= 'Ingreso beneficiarios'
    msg = ''

    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                msg = '<p class="text-danger">DNI o contraseña incorrectos.</p>'
        else:
            msg = '<p class="text-danger">Error al validar los datos.</p>'

    return render(request, "accounts/login.html", {"form": form, "msg": msg, "title":title})

def login_agentes(request):

    form = LoginAgenteForm(request.POST or None)
    title= 'Ingreso agentes'
    msg = 'Ingrese con sus credenciales'

    if request.method == "POST":
        if form.is_valid():

            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")

            ## Validación en Active Directory
            if ADWSLogin(username, password):

                user = authenticate(username=username, password=password)
                if user is None:
                    try:
                        ### Agente registrado con cambio de password
                        user = User.objects.get(username=username)
                        user.set_password(password)
                        user.save()
                        user = authenticate(username=username, password=password)
                        login(request, user)
                        return redirect('/')

                    except User.DoesNotExist:

                        ## Validación para agentes que no pertenecen a SGLP
                        if Usuarios.objects.filter(usrlogin = username).exists():

                            ### Agente no registrado
                            register = SignUpAgenteForm(request.POST)
                            if register.is_valid():
                                data = ADWSGetUsuarioYPass(username)
                                new_user = register.save(commit=False)
                                new_user.first_name = data['Nombre']
                                new_user.last_name = data['Apellido']
                                new_user.save()
                                new_user = authenticate(username=username, password=password)
                                grupo = Group.objects.get(name='Agentes')
                                grupo.user_set.add(new_user)
                                setToken(username,password)
                                login(request, new_user)
                                return redirect('/')
                            else:
                                msg = 'Error al validar los datos.'
                        else:
                            msg = '<p class="text-danger">Agente no autorizado a registrarse en el sistema.d</p>'
                else:
                    ## Agente registrado
                    login(request, user)
                    return redirect("/")
            else:
                msg = '<p class="text-danger">Usuario o contraseña incorrectos.</p>'
        else:
            msg = '<p class="text-danger">Error al validar los datos.</p>'

    return render(request, "accounts/login.html", {"form": form, "msg": msg, "title":title})

def register_beneficiario(request):
    msg = ''
    if request.method == 'POST':
        form = SignUpBeneficiarioForm(request.POST)
        if form.is_valid():
            beneficiario = es_beneficiario(request.POST['username'])
            if beneficiario:
                username = form.cleaned_data.get("username")
                password = form.cleaned_data.get("password1")
                email = form.cleaned_data.get("email")
                user = form.save(commit=False)
                user.first_name = beneficiario[0].get('nombre').title()
                user.last_name = beneficiario[0].get('apellido').title()
                user.save()
                grupo = Group.objects.get(name='Beneficiarios')
                grupo.user_set.add(user)
                setToken(username,password)

                ## Enviar mail
                imgs = ['mail-1.png','mail-2.png','mail-3.png','mail-4.png','mail-5.png','mail-6.png']
                username = user.first_name+' '+user.last_name

                subject = 'SGLP - Registro exitoso'
                text_content = 'SGLP - Envío automático'
                from_email = 'Secretaría de Gobierno Digital <{}>'.format(EMAIL_HOST_USER)
                to_email = email

                t = get_template('layouts/mail.html')
                html = t.render({'user':username,'pass':password})

                mail = EmailMultiAlternatives( subject, text_content, from_email, [to_email] )
                mail.attach_alternative( html, "text/html" )

                for f in imgs:
                    fp = open('apps/static/assets/images/mail/{}'.format(f), 'rb')
                    mail_img = MIMEImage(fp.read())
                    mail_img.add_header('Content-ID', '<{}>'.format(f))
                    mail.attach(mail_img)

                print('Enviando mail...')
                mail.send()

                msg = 'Registro exitoso. <a href="/login_beneficiario" class="text-success"> Iniciar sesión </a>'
            else:
                msg = '<p class="text-danger">Documento no registrado como beneficiario.</p>'
                form = SignUpBeneficiarioForm()
        else:
            msg = '<p class="text-danger">Por favor corrija los errores.</p>'
    else:
        form = SignUpBeneficiarioForm()

    return render(request, 'accounts/register.html', {'form': form, 'msg':msg})
