from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from .forms import createForm
from .models import Perfil
from users.views import index
from Comentario.models import Comentario
from Interaçao.models import Interaçao

# Create your views here.
@login_required
def criar(request):
    if request.method == "POST":
        form = createForm(request.POST, request.FILES)
        if form.is_valid():
            perfil = form.save(commit=False)
            perfil.Usuario = request.user
            perfil.save()
            return redirect(reverse('index'))
    else:
        form = createForm()
    
    return render(request,'Perfil/criar.html', {'form': form})


@login_required
def visualizar(request, id):
   perfil = Perfil.objects.get(pk = id)
   user = request.user
   usuario = Perfil.objects.get(Usuario = user)
   segue = Interaçao.objects.filter(Seguidor=usuario, Pessoa_seguida=perfil)
   lista_comentarios = Comentario.objects.filter(Autor_comentario= perfil).order_by('-Data_criaçao')
   seguidores = Interaçao.objects.filter(Pessoa_seguida=perfil).count()
   seguindo = Interaçao.objects.filter(Seguidor=perfil).count()
   return render(request, 'Perfil/detalhes.html', {'perfil': perfil, 'user':user, 'lista_comentarios':lista_comentarios, 'seguidores':seguidores, 'seguindo': seguindo, 'segue':segue})


@login_required
def meuPerfil(request):
   user = request.user
   perfil = Perfil.objects.get(Usuario=user)
   lista_comentarios = Comentario.objects.filter(Autor_comentario= perfil).order_by('-Data_criaçao')
   seguidores = Interaçao.objects.filter(Pessoa_seguida=perfil).distinct().count()
   seguindo = Interaçao.objects.filter(Seguidor=perfil).distinct().count()
   return render(request, 'Perfil/meuPerfil.html', {'perfil': perfil, 'user':user, 'lista_comentarios':lista_comentarios, 'seguidores':seguidores, 'seguindo': seguindo})


@login_required
def editar(request, id):
    perfil = Perfil.objects.get(pk=id)
    
    if request.method == "POST":
        form = createForm(request.POST,  request.FILES, instance=perfil)
        
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = createForm(instance=perfil)
    
    return render(request, 'Perfil/editar.html', {'form': form, 'perfil': perfil})



#def deletar(request, id):
   # Perfil.objects.get(pk=id).delete()
   # return redirect("/")
