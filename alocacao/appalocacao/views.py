from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import Colaborador


def index(request):
    total_colaboradores_cadastratos = len(Colaborador.objects.values())
    total_colaboradores_ativos = len(Colaborador.objects.all().filter(ativo='sim'))
    output = 'total de colaboradores cadastrados: {}'.format(total_colaboradores_cadastratos)
    output = output + "<br>" + " total de colaboradores ativos: {}".format(total_colaboradores_ativos)
    return HttpResponse(output)

def newAloc(request,name):
    return HttpResponse("Aqui poderá ser cadastrada uma nova alocação para %s" % name)