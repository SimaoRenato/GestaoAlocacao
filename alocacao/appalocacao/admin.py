from django.contrib import admin

# Register your models here.

from .models import Alocacao
from .models import Area
from .models import Colaborador
from .models import Contratos


admin.site.register(Alocacao)
admin.site.register(Area)
admin.site.register(Colaborador)
admin.site.register(Contratos)
