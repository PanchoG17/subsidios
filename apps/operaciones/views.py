from rest_framework import viewsets
from rest_framework import permissions

from .models import Verificacub
from .apis.serializers import VerificacubSerializer

class VerificacubViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Verificacub.objects.all().order_by('-verificacubfchtrn')
    serializer_class = VerificacubSerializer
    permission_classes = [permissions.IsAuthenticated]