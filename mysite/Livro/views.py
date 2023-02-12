from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import createForm
from .models import Livro
# Create your views here.

def criar(request):
    if request.method == "POST":
        form = createForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = createForm()
    
    return render(request,'Livro/criar.html', {'form': form})


def listar(request):
    listaLivros = Livro.objects.all()
    return render(request,'Livro/listar.html', {'lista': listaLivros})
    

def expandir(request, id):
    livro = Livro.objects.get(pk = id)
    return render(request, 'Livro/detalhes.html', {'livro': livro})

def editar(request, id):
    livro = Livro.objects.get(pk=id)
    
    if request.method == "POST":
        form = createForm(request.POST, instance=livro)
        
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = createForm(instance=livro)
    
    return render(request, 'Livro/editar.html', {'form': form})



def deletar(request, id):
    Livro.objects.get(pk=id).delete()
    return redirect("/livros/")
