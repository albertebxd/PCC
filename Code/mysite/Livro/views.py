from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth.decorators import login_required
from .forms import createForm
from .models import Livro
from Perfil.models import Perfil
from Leitura.models import Leitura
from Comentario.models import Comentario
# Create your views here.
@login_required
def criar(request):
    if request.method == "POST":
        form = createForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/livros/')
    else:
        form = createForm()
    
    return render(request,'Livro/criar.html', {'form': form})

@login_required
def listar(request):
    user = request.user
    p = get_object_or_404(Perfil, Usuario=user)
    
    pesquisa = request.GET.get('pesquisa')

    if pesquisa:
        listaLivros = Livro.objects.filter(Titulo__icontains=pesquisa, is_valid='True')
    else:
       listaLivros = Livro.objects.filter(is_valid='True')

    if user.is_superuser:
        return render(request,'Livro/listar-adm.html', {'lista': listaLivros, 'p': p})
    else:
        return render(request,'Livro/listar.html', {'lista': listaLivros, 'p': p})


def listar_solicitacoes(request):
    user = request.user
    p = get_object_or_404(Perfil, Usuario=user)

    pesquisa = request.GET.get('pesquisa')

    if pesquisa:
        listaLivros = Livro.objects.filter(Titulo__icontains=pesquisa, is_valid='False')
    else:
       listaLivros = Livro.objects.filter(is_valid='False')

    return render(request,'Livro/listarSolicitaçoes.html', {'lista': listaLivros, 'p': p})


def validar_solicitaçao(request, id_livro):
    livro = Livro.objects.get (pk=id_livro)
    livro.is_valid = 'True'
    livro.save()
    return redirect('/livros/solicitaçoes/')


@login_required
def expandir(request, id):
    user = request.user
    p = get_object_or_404(Perfil, Usuario=user)
    livro = Livro.objects.get(pk = id)
    lista_comentarios = Comentario.objects.filter(Livro_comentario = livro)
    leituras = Leitura.objects.filter(Livro_lido = livro)
    cont =0
    soma_avaliacoes =0
    
    for i in leituras:
        cont=cont+1
        soma_avaliacoes = soma_avaliacoes + i.Avaliacao
    
    if cont==0:
        media=0
    else:
        media = soma_avaliacoes/cont
        
    if user.is_superuser:
        return render(request, 'Livro/detalhes-adm.html', {'livro': livro, 'p': p, 'media': media, 'cont' : cont, 'lista_comentarios' : lista_comentarios})
    else:
        return render(request, 'Livro/detalhes.html', {'livro': livro, 'p': p, 'media': media, 'cont' : cont, 'lista_comentarios' : lista_comentarios})
    

@login_required
def editar(request, id):
    livro = Livro.objects.get(pk=id)
    
    if request.method == "POST":
        form = createForm(request.POST, request.FILES,  instance=livro)
        
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = createForm(instance=livro)
    
    return render(request, 'Livro/editar.html', {'form': form, 'livro': livro})


@login_required
def deletar(request, id):
    Livro.objects.get(pk=id).delete()
    return redirect("/livros/")
