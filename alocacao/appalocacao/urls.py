from django.urls import path

from . import views
from .views import TabelaAlocacaoListView

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:name>', views.newAloc, name='newAloc'),
    path('alocacao/', TabelaAlocacaoListView.as_view()),
]