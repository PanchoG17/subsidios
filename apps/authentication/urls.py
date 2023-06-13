from django.urls import path
from .views import login_home, login_agentes, login_beneficiarios, register_beneficiario
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', login_home, name="login"),
    path('login_agente/', login_agentes, name="login_agente"),
    path('login_beneficiario/', login_beneficiarios, name="login_beneficiario"),
    path('register_beneficiario/', register_beneficiario, name="register_beneficiario"),
    path("logout/", LogoutView.as_view(), name="logout")
]
