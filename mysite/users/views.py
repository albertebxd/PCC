from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from Perfil.models import Perfil
# Create your views here.

def index(request):
    return render(request, 'index.html')


@login_required
def home(request):
    u = request.user
    perfil_existe = Perfil.objects.filter(Usuario=u)
    if perfil_existe:
        return render(request, 'home.html')
    else: 
        return redirect('/perfil/criar/')


class cadastro(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'cadastro.html'

