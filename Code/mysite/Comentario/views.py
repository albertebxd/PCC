
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .forms import createForm, createForm2
from .models import Comentario
from Livro.models import Livro 
from Perfil.models import Perfil
from Perfil.views import listarPerfis
from Interaçao.models import Interaçao
from Leitura.models import Leitura
# Create your views here.


@login_required
def criar(request, id_livro):
    if request.method == "POST":
        form = createForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)

            user = request.user
            f.Autor_comentario = get_object_or_404(Perfil, Usuario=user)

            f.save()
            return redirect('/')
    else:
        form = createForm()
    
    return render(request,'Comentario/criar.html', {'form': form})


@login_required
def editar(request, id):
    comentario = Comentario.objects.get(pk=id)
    
    if request.method == "POST":
        form = createForm(request.POST, instance=comentario)
        
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = createForm(instance=comentario)
    
    return render(request, 'Comentario/editar.html', {'form': form, 'comentario':comentario})

@login_required
def listar(request):

    if request.method == "POST":
        form = createForm2(request.POST)
        if form.is_valid():
            f = form.save(commit=False)

            user = request.user
            f.Autor_comentario = get_object_or_404(Perfil, Usuario=user)

            f.save()
            return redirect('/')
    else:
        form = createForm2()
    

    pesquisa = request.GET.get('pesquisa')
    if pesquisa:
        return redirect(reverse('listarPerfis', args=[pesquisa]))


    user = request.user
    perfil = get_object_or_404(Perfil, Usuario=user)
    lista = Comentario.objects.all().order_by('-Data_criaçao')
    page = request.GET.get('page', 1)
    pagination = Paginator(lista, 5)
    page_obj = pagination.get_page(page)
    seguidores = Interaçao.objects.filter(Pessoa_seguida=perfil).distinct().count()
    seguindo = Interaçao.objects.filter(Seguidor=perfil).distinct().count()
    lista_leitura = Leitura.objects.filter(Leitor=perfil, Status='Lido') | Leitura.objects.filter(Leitor=perfil, Status='Lendo')
    top_livros = Livro.objects.all().order_by('-Quant_leituras')[:5]
    return render(request,'Comentario/listar.html', {'page_obj':page_obj, 'lista': lista, 'lista_leitura':lista_leitura, 'top_livros':top_livros,  'p':perfil, 'seguindo':seguindo, 'seguidores':seguidores})


@login_required
def deletar(request, id):
    Comentario.objects.get(pk=id).delete()
    return redirect("/perfil/meuPerfil/")


@login_required
def curtir(request, id):
    u = request.user
    perfil = get_object_or_404(Perfil, Usuario=u)
    comentario = get_object_or_404(Comentario, id=id)
    comentario.Curtida.add(perfil)
    comentario.save()
    return redirect('/')