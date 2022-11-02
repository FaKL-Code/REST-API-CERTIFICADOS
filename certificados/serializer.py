from rest_framework import serializers
from certificados.models import Certificado

class CertificadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificado
        fields = ['id', 'nome_do_curso', 'carga_horaria', 'instituicao', 'certificado']