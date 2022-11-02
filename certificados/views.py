from certificados.models import Certificado
from certificados.serializer import CertificadoSerializer
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class CertificadosViewSet(viewsets.ModelViewSet):
    
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
    queryset = Certificado.objects.all()
    
    def get_serializer_class(self):
        return CertificadoSerializer    
