from django.urls import path
from galeria.views import index, imagem

urlpatterns = [
    path('', index, name='index'), # Quando o usuário acessar a rota /index, ele será redirecionado para a função index do arquivo views.py
    path('imagem/<int:foto_id>', imagem, name='imagem') # Quando o usuário acessar a rota /imagem, ele será redirecionado para a função imagem do arquivo views.py
]