from certificados.models import Certificado
from certificados.serializer import CertificadoSerializer
from rest_framework import viewsets


class CertificadosViewSet(viewsets.ModelViewSet):
    
    queryset = Certificado.objects.all()
    
    def get_serializer_class(self):
        return CertificadoSerializer    
