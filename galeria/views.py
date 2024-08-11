# Este arquivo é responsável por definir as rotas da aplicação.
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'galeria/index.html') # Renderiza o arquivo index.html

def imagem(request):
    return render(request, 'galeria/imagem.html') # Renderiza o arquivo imagem.html