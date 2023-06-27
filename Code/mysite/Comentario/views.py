
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import createForm, createForm2
from .models import Comentario
from Livro.models import Livro 
from Perfil.models import Perfil
from Interaçao.models import Interaçao
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
    
    user = request.user
    perfil = get_object_or_404(Perfil, Usuario=user)
    lista = Comentario.objects.all().order_by('-Data_criaçao')
    seguidores = Interaçao.objects.filter(Pessoa_seguida=perfil).distinct().count()
    seguindo = Interaçao.objects.filter(Seguidor=perfil).distinct().count()
    lista_livros = Livro.objects.all()
    top_livros = lista_livros.order_by('-Quant_leituras')[:5]
    return render(request,'Comentario/listar.html', {'lista': lista, 'lista_livros':lista_livros, 'top_livros':top_livros,  'p':perfil, 'seguindo':seguindo, 'seguidores':seguidores})


@login_required
def deletar(request, id):
    Comentario.objects.get(pk=id).delete()
    return redirect("/leituras/")


@login_required
def curtir(request, id):
    u = request.user
    perfil = get_object_or_404(Perfil, Usuario=u)
    comentario = get_object_or_404(Comentario, id=id)
    comentario.Curtida.add(perfil)
    comentario.save()
    return redirect('/')