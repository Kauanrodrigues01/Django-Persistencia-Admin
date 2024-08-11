# Este arquivo é responsável por definir as rotas da aplicação.
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('galeria.urls')), # Quando o usuário acessar a raiz do site, ele será redirecionado para o arquivo urls.py da aplicação galeria
    path('galeria/', include('galeria.urls')), # Quando o usuário acessar a rota /galeria, ele será redirecionado para o arquivo urls.py da aplicação galeria
]
