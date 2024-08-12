from django.contrib import admin
from galeria.models import Fotografia

# Register your models here.

class ListandoFotografias(admin.ModelAdmin):
    list_display = ('id', 'nome', 'categoria','legenda', 'descricao', 'foto', 'publicada') # Define quais campos serão exibidos na listagem de fotografias no painel administrativo
    list_display_links = ('id', 'nome') # Define quais campos serão clicáveis na listagem de fotografias no painel administrativo
    search_fields = ('nome',) # Define quais campos serão pesquisáveis na listagem de fotografias no painel administrativo
    list_filter = ('categoria',) # Define quais campos serão filtráveis na listagem de fotografias no painel administrativo
    list_per_page = 15 # Define quantos registros serão exibidos por página na listagem de fotografias no painel administrativo

admin.site.register(Fotografia, ListandoFotografias) # Registra o modelo Fotografia no painel administrativo do Django