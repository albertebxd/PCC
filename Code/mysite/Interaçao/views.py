from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Interaçao
from Perfil.models import Perfil
# Create your views here.


@login_required
def criar(request, id_pessoa):
    u = request.user
    perfil_seguidor = get_object_or_404(Perfil, Usuario=u)
    perfil_seguido = get_object_or_404(Perfil, id = id_pessoa)

    a = Interaçao(Seguidor=perfil_seguidor, Pessoa_seguida=perfil_seguido)
    a.save()
    return redirect("/")


@login_required
def deletar(request, id_pessoa):
    perfil_seguido = get_object_or_404(Perfil, id = id_pessoa)
    Interaçao.objects.get(Pessoa_seguida = perfil_seguido).delete()
    
    return redirect("/")