from django.urls import include, path
from . import views

urlpatterns = [
   path('criar/', views.criar, name='criar'),
   path('listar/<str:pesquisa>', views.listarPerfis, name='listarPerfis'),
   path('visualizar/<int:id>', views.visualizar, name='visualizar'),
   path('editar/<int:id>', views.editar, name='editar'),
   path('meuPerfil/', views.meuPerfil, name='meuPerfil'),
   # path('deletar/<int:id>', views.deletar, name='deletar')

]