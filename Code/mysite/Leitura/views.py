from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import createForm
from .models import Leitura
from Livro.models import Livro 
from Perfil.models import Perfil
from django.utils import timezone
# Create your views here.

@login_required
def criar(request, id_livro):
    if request.method == "POST":
        form = createForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)

            user = request.user
            f.Leitor = get_object_or_404(Perfil, Usuario=user)

            livro = get_object_or_404(Livro, pk=id_livro)
            f.Livro_lido = livro
            livro.Quant_leituras +=1
            livro.save()

            f.save()
            return redirect('/')
    else:
        form = createForm()
    
    return render(request,'Leitura/criar.html', {'form': form})

@login_required
def listar(request):
    user = request.user
    perfil = get_object_or_404(Perfil, Usuario=user)
    lista = Leitura.objects.filter(Leitor=perfil)
    return render(request,'Leitura/listar.html', {'lista': lista,  'p':perfil})

@login_required
def listar_lidos(request):
    user = request.user
    perfil = get_object_or_404(Perfil, Usuario=user)
    lista = Leitura.objects.filter(Leitor=perfil, Status='Lido')
    return render(request,'Leitura/listar.html', {'lista': lista,  'p':perfil})

@login_required
def listar_lendo(request):
    user = request.user
    perfil = get_object_or_404(Perfil, Usuario=user)
    lista = Leitura.objects.filter(Leitor=perfil, Status='Lendo')
    return render(request,'Leitura/listar.html', {'lista': lista,  'p':perfil})

@login_required
def listar_queroLer(request):
    user = request.user
    perfil = get_object_or_404(Perfil, Usuario=user)
    lista = Leitura.objects.filter(Leitor=perfil, Status='Quero ler')
    return render(request,'Leitura/listar.html', {'lista': lista,  'p':perfil})


@login_required
def editar(request, id):
    leitura = Leitura.objects.get(pk=id)
    
    if request.method == "POST":
        form = createForm(request.POST, instance=leitura)
        
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = createForm(instance=leitura)
    
    return render(request, 'Leitura/editar.html', {'form': form, 'leitura':leitura})

@login_required
def deletar(request, id):
    leitura = Leitura.objects.get(pk=id)
    livro = get_object_or_404(Livro, pk=leitura.Livro_lido.id)
    livro.Quant_leituras -=1
    livro.save()
    leitura.delete()
    return redirect("/leituras/")

@login_required
def finalizar_leitura(request, id):
    leitura = Leitura.objects.get(pk=id)
    leitura.Data_final = timezone.now()
    leitura.save()
    return redirect("/leituras/")
