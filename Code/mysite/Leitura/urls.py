from django.urls import include, path
from . import views

urlpatterns = [
    path('criar/<int:id_livro>', views.criar, name='criar'),
    path('', views.listar, name='listar'),
    #path('expandir/<int:id>', views.expandir, name='expandir'),
    path('editar/<int:id>', views.editar, name='editar'),
    path('deletar/<int:id>', views.deletar, name='deletar'),
    path('finalizar/<int:id>', views.finalizar_leitura, name='finalizar_leitura'),
    path('iniciar/<int:id>', views.iniciar_leitura, name='iniciar_leitura'),
    path('lidos/', views.listar_lidos, name='listar_lidos'),
    path('lendo/', views.listar_lendo, name='listar_lendo'),
    path('quero/', views.listar_queroLer, name='listar_queroLer'),
    path('criarMeta/<int:id>', views.meta_leitura, name='meta_leitura'),
    path('editarMeta/<int:id>', views.editarMeta_leitura, name='editarMeta_leitura'),
    path('lidos/<int:id>', views.listar_lidos_visitante, name='listar_lidos_visitante'),
    path('lendo/<int:id>', views.listar_lendo_visitante, name='listar_lendo_visitante'),
    path('quero/<int:id>', views.listar_queroLer_visitante, name='listar_queroLer_visitante'),
    path('<int:id>', views.listar_visitante, name='listar_visitante')
]
