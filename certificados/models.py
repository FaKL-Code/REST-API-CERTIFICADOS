from django.db import models

class Certificado(models.Model):
    nome_do_curso = models.CharField(max_length=40)
    carga_horaria = models.CharField(max_length = 5)
    instituicao = models.CharField(max_length = 30)
    certificado = models.FileField(blank=False)
    
    def __str__(self):
        return self.nome_do_curso
