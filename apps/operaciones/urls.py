from django.urls import path
from rest_framework import routers
from apps.operaciones import views

router = routers.DefaultRouter()
router.register(r'verificacub', views.VerificacubViewSet)

app_name = 'operaciones'
urlpatterns = [
    
]