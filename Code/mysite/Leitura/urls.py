from django.urls import include, path
from . import views

urlpatterns = [
    path('criar/<int:id_livro>', views.criar, name='criar'),
    path('', views.listar, name='listar'),
    #path('expandir/<int:id>', views.expandir, name='expandir'),
    path('editar/<int:id>', views.editar, name='editar'),
    path('deletar/<int:id>', views.deletar, name='deletar'),
    path('finalizar/<int:id>', views.finalizar_leitura, name='finalizar_leitura'),
    path('lidos', views.listar_lidos, name='listar_lidos'),
    path('lendo', views.listar_lendo, name='listar_lendo'),
    path('quero', views.listar_queroLer, name='listar_queroLer')
]
