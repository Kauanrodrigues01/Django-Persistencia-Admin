# Este arquivo é responsável por definir as rotas da aplicação.
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from galeria.models import Fotografia


def index(request):
    fotografias = Fotografia.objects.order_by('data_fotografia').filter(publicada=True) # Busca todas as fotografias no banco de dados e ordena por data de fotografia, se colocar um - antes de data_fotografia, ele ordena de forma decrescente
    return render(request, 'galeria/index.html', {'cards': fotografias}) # Renderiza o arquivo index.html

def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id) # Busca a fotografia no banco de dados pelo id
    return render(request, 'galeria/imagem.html', {'fotografia': fotografia}) # Renderiza o arquivo imagem.html e passa a fotografia como contexto para o template HTML, que será acessível através da variável fotografia

def buscar(request):
    todas_fotografias = Fotografia.objects.order_by('data_fotografia').filter(publicada=True)
    
    if 'buscar' in request.GET:
        nome = request.GET['buscar']
        if nome:
            fotografias = todas_fotografias.filter(nome__icontains=nome) | todas_fotografias.filter(descricao__icontains=nome)
            return render(request, 'galeria/buscar.html', {'cards': fotografias})
    
    return render(request, 'galeria/buscar.html')  # Renderiza o arquivo buscar.html