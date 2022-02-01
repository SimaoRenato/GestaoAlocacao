from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import Colaborador
from .models import Alocacao
from django.views.generic import ListView


class TabelaAlocacaoListView(ListView):
    model = Colaborador
    template_name = 'templates/tabela_alocacao.html'


def index(request):
    colab = Colaborador.objects.all()
    total_colaboradores_cadastratos = len(colab)
    total_colaboradores_ativos = len(colab.filter(ativo='sim'))
    output = 'total de colaboradores cadastrados: {}'.format(total_colaboradores_cadastratos)
    output = output + "<br>" + " total de colaboradores ativos: {}".format(total_colaboradores_ativos)
    output = output + "<br><br> <h1> Lista de colaboradores cadastrados: </h1>"

    for nome in colab:
        output = output + "<br>" + nome.nomecolaborador

    output = output + "<br><br> <h1> Lista de colaboradores ativos:</h1>"

    for i in colab.filter(ativo='sim'):
        output = output + "<br>" + i.nomecolaborador

    return HttpResponse(output)


def newAloc(request,name):
    return HttpResponse("Aqui poderá ser cadastrada uma nova alocação para %s" % name)

