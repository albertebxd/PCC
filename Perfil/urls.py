from django.urls import include, path
from . import views

urlpatterns = [
   path('criar/', views.criar, name='criar'),
   # path('', views.listar, name='listar'),
   path('visualizar/<int:id>', views.visualizar, name='visualizar'),
   path('editar/<int:id>', views.editar, name='editar'),
   # path('deletar/<int:id>', views.deletar, name='deletar')

]