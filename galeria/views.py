# Este arquivo é responsável por definir as rotas da aplicação.
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from galeria.models import Fotografia


def index(request):
    fotografias = Fotografia.objects.all() # Busca todas as fotografias no banco de dados
    return render(request, 'galeria/index.html', {'cards': fotografias}) # Renderiza o arquivo index.html

def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id) # Busca a fotografia no banco de dados
    return render(request, 'galeria/imagem.html', {'fotografia': fotografia}) # Renderiza o arquivo imagem.html e passa a fotografia como contexto para o template HTML, que será acessível através da variável fotografia