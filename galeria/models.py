from django.db import models

# Create your models here.
class Fotografia(models.Model): # Define a classe fotografia, que herda de models.Model, models.Model é uma classe do Django que define um modelo de banco de dados.
    OPCOES_CATEGORIA = [ # Define as opções de categoria que serão exibidas no formulário de cadastro de fotografias
        ('NEBULOSA', 'Nebulosa'),
        ('GALÁXIA', 'Galáxia'),
        ('PLANETA', 'Planeta'),
        ('ESTRELA', 'Estrela'),
        ('OUTRO', 'Outro'),
    ]
    
    nome = models.CharField(max_length=100, null=False, blank=False)
    legenda = models.CharField(max_length=200, null=False, blank=False)
    categoria = models.CharField(max_length=100,choices=OPCOES_CATEGORIA, default='')
    descricao = models.TextField(null=False, blank=False)
    foto = models.CharField(max_length=100, null=False, blank=False)
    publicada = models.BooleanField(default=False)

    def __str__(self):
        return f'Fotografia: [nome={self.nome}]'