# Este arquivo é responsável por definir as rotas da aplicação.
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('galeria.urls')), # Quando o usuário acessar a raiz do site, ele será redirecionado para o arquivo urls.py da aplicação galeria
    path('galeria/', include('galeria.urls')), # Quando o usuário acessar a rota /galeria, ele será redirecionado para o arquivo urls.py da aplicação galeria
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # Adiciona a rota para servir arquivos de mídia
