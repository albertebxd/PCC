from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import createForm
from .models import Livro
from Perfil.models import Perfil
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
        listaLivros = Livro.objects.filter(Titulo__icontains=pesquisa)
    else:
       listaLivros = Livro.objects.all()

    return render(request,'Livro/listar.html', {'lista': listaLivros, 'p': p})
    
@login_required
def expandir(request, id):
    user = request.user
    p = get_object_or_404(Perfil, Usuario=user)
    livro = Livro.objects.get(pk = id)
    return render(request, 'Livro/detalhes.html', {'livro': livro, 'p': p})

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
