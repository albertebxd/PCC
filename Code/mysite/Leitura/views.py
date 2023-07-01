from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import createForm, createForm_meta, editarForm
from django.core.paginator import Paginator
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
            return redirect('/leituras/')
    else:
        form = createForm()
    
    return render(request,'Leitura/criar.html', {'form': form})

@login_required
def listar(request):
    user = request.user
    perfil = get_object_or_404(Perfil, Usuario=user)
    lista = Leitura.objects.filter(Leitor=perfil)
    page = request.GET.get('page', 1)
    pagination = Paginator(lista, 9)
    page_obj = pagination.get_page(page)
    return render(request,'Leitura/listar.html', {'page_obj': page_obj, 'lista': lista,  'p':perfil})


@login_required
def listar_lidos(request):
    user = request.user
    perfil = get_object_or_404(Perfil, Usuario=user)
    lista = Leitura.objects.filter(Leitor=perfil, Status='Lido')
    return render(request,'Leitura/listar_lidos.html', {'lista': lista,  'p':perfil})


@login_required
def listar_lendo(request):
    user = request.user
    perfil = get_object_or_404(Perfil, Usuario=user)
    lista = Leitura.objects.filter(Leitor=perfil, Status='Lendo')
    return render(request,'Leitura/listar_lendo.html', {'lista': lista,  'p':perfil})
   

@login_required
def listar_queroLer(request):
    user = request.user
    perfil = get_object_or_404(Perfil, Usuario=user)
    lista_esseMes = Leitura.objects.filter(Leitor=perfil, Status='Quero ler', Meta_leitura="Esse mês")
    lista_proxMes = Leitura.objects.filter(Leitor=perfil, Status='Quero ler', Meta_leitura="Próximo mês")
    lista_esseAno = Leitura.objects.filter(Leitor=perfil, Status='Quero ler', Meta_leitura="Esse ano")
    lista_proxAno = Leitura.objects.filter(Leitor=perfil, Status='Quero ler', Meta_leitura="Próximo ano")
    lista_naoSei = Leitura.objects.filter(Leitor=perfil, Status='Quero ler', Meta_leitura="Não sei ")
    return render(request,'Leitura/listar_queroLer.html', {'lista_esseMes': lista_esseMes, 'lista_proxMes': lista_proxMes, 'lista_esseAno': lista_esseAno, 'lista_proxAno': lista_proxAno, 'lista_naoSei': lista_naoSei, 'p':perfil})

@login_required
def editar(request, id):
    leitura = Leitura.objects.get(pk=id)
    
    if request.method == "POST":
        form = createForm(request.POST, instance=leitura)
        
        if form.is_valid():
            form.save()
            return redirect("/leituras/")
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
    leitura.Status = 'Lido'
    leitura.save()
    return redirect("/leituras/")

@login_required
def iniciar_leitura(request, id):
    leitura = Leitura.objects.get(pk=id)
    leitura.Status = 'Lendo'
    leitura.Data_inicio = timezone.now()
    leitura.save()
    return redirect("/leituras/")


@login_required
def meta_leitura(request, id):

    if request.method == "POST":
        form = createForm_meta(request.POST)
        
        if form.is_valid():
            f = form.save(commit=False)

            user = request.user
            f.Leitor = get_object_or_404(Perfil, Usuario=user)
            f.Livro_lido = get_object_or_404(Livro, pk=id)
            f.Status = 'Quero ler'

            f.save()
            return redirect('/')
    else:
        form = createForm_meta()
    
    return render(request,'Leitura/metaLeitura.html', {'form': form})


@login_required
def editarMeta_leitura(request, id):
    leitura = Leitura.objects.get(pk=id)
    
    if request.method == "POST":
        form = editarForm(request.POST, instance=leitura)
        
        if form.is_valid():
            form.save()
            return redirect("/leituras/")
    else:
        form = editarForm(instance=leitura)
    
    return render(request, 'Leitura/editarMeta.html', {'form': form, 'leitura':leitura})


    
@login_required
def listar_visitante(request, id):
    user = request.user
    usuario = get_object_or_404(Perfil, Usuario=user)
    perfil = get_object_or_404(Perfil,id=id)
    lista = Leitura.objects.filter(Leitor=perfil)
    page = request.GET.get('page', 1)
    pagination = Paginator(lista, 9)
    page_obj = pagination.get_page(page)
    return render(request,'Leitura/listarVisitante.html', {'page_obj': page_obj, 'lista': lista,  'p':usuario, 'perfil_visitado':perfil})


@login_required
def listar_lidos_visitante(request, id):
    user = request.user
    usuario = get_object_or_404(Perfil, Usuario=user)
    perfil = get_object_or_404(Perfil,id=id)
    lista = Leitura.objects.filter(Leitor=perfil, Status='Lido')
    return render(request,'Leitura/listar_lidosVisitante.html', {'lista': lista,  'p':usuario, 'perfil_visitado':perfil})


@login_required
def listar_lendo_visitante(request, id):
    user = request.user
    usuario = get_object_or_404(Perfil, Usuario=user)
    perfil = get_object_or_404(Perfil,id=id)
    lista = Leitura.objects.filter(Leitor=perfil, Status='Lendo')
    return render(request,'Leitura/listar_lendoVisitante.html', {'lista': lista,  'p':usuario, 'perfil_visitado':perfil})
   

@login_required
def listar_queroLer_visitante(request, id):
    user = request.user
    usuario = get_object_or_404(Perfil, Usuario=user)
    perfil = get_object_or_404(Perfil,id=id)
    lista_esseMes = Leitura.objects.filter(Leitor=perfil, Status='Quero ler', Meta_leitura="Esse mês")
    lista_proxMes = Leitura.objects.filter(Leitor=perfil, Status='Quero ler', Meta_leitura="Próximo mês")
    lista_esseAno = Leitura.objects.filter(Leitor=perfil, Status='Quero ler', Meta_leitura="Esse ano")
    lista_proxAno = Leitura.objects.filter(Leitor=perfil, Status='Quero ler', Meta_leitura="Próximo ano")
    lista_naoSei = Leitura.objects.filter(Leitor=perfil, Status='Quero ler', Meta_leitura="Não sei ")
    return render(request,'Leitura/listar_queroLerVisitante.html', {'lista_esseMes': lista_esseMes, 'lista_proxMes': lista_proxMes, 'lista_esseAno': lista_esseAno, 'lista_proxAno': lista_proxAno, 'lista_naoSei': lista_naoSei, 'p':usuario, 'perfil_visitado':perfil})