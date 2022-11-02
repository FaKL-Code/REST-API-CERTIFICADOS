from django.contrib import admin
from certificados.models import Certificado

class Certificados(admin.ModelAdmin):
    list_display = ('id', 'nome_do_curso', 'carga_horaria', 'instituicao')
    list_display_links = ('id', 'nome_do_curso')
    search_fields = ('nome_do_curso',)
    list_per_page = 20
    
admin.site.register(Certificado, Certificados)