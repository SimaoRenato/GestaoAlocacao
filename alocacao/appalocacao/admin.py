from django.contrib import admin

# Register your models here.

from .models import Alocacao
from .models import Area
from .models import Colaborador
from .models import Contratos
from .models import Tipoalocacao
from .models import Valorhora
from .models import Projetos
from .models import Equipe

class AlocacaoAdmin(admin.ModelAdmin):
    list_display = ['colaborador_matricula','id_projetos','horas','mes_ano','tipoalocacao_idtipoalocacao']
admin.site.register(Alocacao,AlocacaoAdmin)

admin.site.register(Area)

class ColaboradorAdmin(admin.ModelAdmin):
    list_display = ['matricula','nomecolaborador','id_contrato','id_area','id_equipe','ativo']

admin.site.register(Colaborador,ColaboradorAdmin)

admin.site.register(Contratos)

class ProjetosAdmin(admin.ModelAdmin):
    list_display = ['idprojetos','nomeprojeto','empresa','statusprojetos']
admin.site.register(Projetos,ProjetosAdmin)

admin.site.register(Tipoalocacao)
admin.site.register(Valorhora)
admin.site.register(Equipe)