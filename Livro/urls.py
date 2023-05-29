from django.urls import include, path
from . import views

urlpatterns = [
    path('criar/', views.criar, name='criar'),
    path('', views.listar, name='listar'),
    path('expandir/<int:id>', views.expandir, name='expandir'),
    path('editar/<int:id>', views.editar, name='editar'),
    path('deletar/<int:id>', views.deletar, name='deletar'),
    path('solicitaçoes/', views.listar_solicitacoes, name='listar_solicitaçoes'),
    path('validar/<int:id_livro>', views.validar_solicitaçao, name='validar_solicitaçao')

]
