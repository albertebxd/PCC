from django.urls import include, path
from . import views

urlpatterns = [
    path('criar/<int:id_livro>', views.criar, name='criar'),
    path('', views.listar, name='listar'),
    path('editar/<int:id>', views.editar, name='editar'),
    path('deletar/<int:id>', views.deletar, name='deletar'),
    path('curtir/<int:id>', views.curtir, name='curtir')
]
