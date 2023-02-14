from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from .forms import createForm
from .models import Perfil
from users.views import index
# Create your views here.
@login_required
def criar(request):
    if request.method == "POST":
        form = createForm(request.POST)
        if form.is_valid():
            perfil = form.save(commit=False)
            perfil.Usuario = request.user
            perfil.save()
            return redirect(reverse('index'))
    else:
        form = createForm()
    
    return render(request,'Perfil/criar.html', {'form': form})

def visualizar(request, id):
   perfil = Perfil.objects.get(pk = id)
   return render(request, 'Perfil/detalhes.html', {'perfil': perfil})

def editar(request, id):
    perfil = Perfil.objects.get(pk=id)
    
    if request.method == "POST":
        form = createForm(request.POST, instance=perfil)
        
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = createForm(instance=perfil)
    
    return render(request, 'Perfil/editar.html', {'form': form})



#def deletar(request, id):
   # Perfil.objects.get(pk=id).delete()
   # return redirect("/")
