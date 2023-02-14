from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from Perfil.models import Perfil
from Leitura.views import listar
# Create your views here.

def index(request):
    if request.user.is_authenticated:
        u = request.user
        perfil_existe = Perfil.objects.filter(Usuario=u)
        if perfil_existe:
            return redirect(reverse('listar', ))
        else: 
            return redirect('/perfil/criar/')
    else:
        return render(request, 'index.html')



class cadastro(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'cadastro.html'

