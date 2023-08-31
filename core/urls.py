from django.urls import path
from core import views
from django.contrib.auth.views import LoginView



urlpatterns = [
    path('',views.index, name='index'),
    path('ativos/', views.lista_ativos, name='lista-ativos'),
    path('ativos/adicionar/', views.adicionar_ativo, name='adicionar-ativo'),
    path('editar-ativo/<int:ativo_id>/', views.editar_ativo, name='editar-ativo'),
    path('ativos/excluir/<int:id>/', views.excluir_ativo, name='excluir-ativo'),
    path('login/', LoginView.as_view(), name='login'),
    path('cadastro/', views.cadastros_view, name='cadasto'),
    path('pesquisar/', views.pesquisar_ativos, name='pesquisar'),
    path('manutencoes/', views.lista_manutencoes, name='lista-manutencoes'),
    path('adicionar-manutencao/', views.adicionar_manutencao, name='adicionar-manutencao'),
]


