from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
   # path('home/', views.home, name='home'),
    path('cadastro/', views.cadastro.as_view(), name='cadastro'),
    
]
