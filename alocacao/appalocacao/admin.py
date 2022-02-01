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

admin.site.register(Alocacao)
admin.site.register(Area)
admin.site.register(Colaborador)
admin.site.register(Contratos)
admin.site.register(Projetos)
admin.site.register(Tipoalocacao)
admin.site.register(Valorhora)
admin.site.register(Equipe)