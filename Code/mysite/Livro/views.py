from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Avg, Sum
from .forms import createForm
from .models import Livro
from Perfil.models import Perfil
from Leitura.models import Leitura
from Comentario.models import Comentario
from Comentario.forms import createForm
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
    if request.method == "POST":
        form = createForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)

            user = request.user
            f.Autor_comentario = get_object_or_404(Perfil, Usuario=user)
            f.Livro_comentario = get_object_or_404(Livro, pk=id)
            f.save()
            return redirect(reverse('expandir', args=[id])) 
    else:
        form = createForm()

    user = request.user
    p = get_object_or_404(Perfil, Usuario=user)
    livro = Livro.objects.get(pk = id)
    lista_comentarios = Comentario.objects.filter(Livro_comentario = livro).order_by('-Data_criaçao')
    page = request.GET.get('page', 1)
    pagination = Paginator(lista_comentarios, 3)
    page_obj = pagination.get_page(page)
    cont_leituras = Leitura.objects.filter(Livro_lido = livro).count()
    media_avaliacoes = Leitura.objects.filter(Livro_lido = livro).aggregate(Sum('Avaliacao'))['Avaliacao__sum'] or 0
    if user.is_superuser:
        return render(request, 'Livro/detalhes-adm.html', {'page_obj':page_obj, 'livro': livro, 'p': p, 'media_avaliacoes': media_avaliacoes, 'cont_leituras' : cont_leituras, 'lista_comentarios' : lista_comentarios })
    else:
        return render(request, 'Livro/detalhes.html', {'page_obj':page_obj, 'livro': livro, 'p': p, 'media_avaliacoes': media_avaliacoes, 'cont_leituras' : cont_leituras, 'lista_comentarios' : lista_comentarios})
    

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
