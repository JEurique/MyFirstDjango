""" Django file for views """
from django.shortcuts import render
from django.http import HttpResponse
from .models import Pessoa

# Create your views here.

def index(request):
    """ Index """
    return HttpResponse("Hello, world. You're at the polls index.")

def listar_registros(request):
    """ Listar Registros """
    pessoas = Pessoa.objects.all()
    lista_pessoas = []
    for pess in pessoas:
        lista_pessoas.append('Olá, teste, eu sou {nome}'.format(nome=pess.nome))
    return render(request, 'list.html', {'pessoas': lista_pessoas})
