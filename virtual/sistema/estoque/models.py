from django.db import models
from django import forms
from django.utils import timezone

class Produto(models.Model):
	"""docstring for Agepen"""
	
	#grupos de produtos
	GRUPOS = (
		('ACES','Acessórios'),
	    ('PCIM','Partes de cima'),
	    ('PBAI','Partes de baixo')
	)

	#categorias de produtos
	CATEGORIAS = (
		('CAMT','Camisetas'),
	    ('BLUS','Blusinhas'),
	    ('CAMI','Camisas'),
	    ('SUCA','Suéteres e cardigans'),
	    ('BLJC','Blazers, jaquetas e casacos'),
	    ('COLQ','Coletes e quimonos'),
	    ('REGA','Regatas'),

		('SHBE','Shorts e bermudas'),
	    ('CALC','Calças'),
	    ('VEST','Vestidos'),
	    ('SAIA','Saias'),

		('MAIC','Meias-calças'),
	    ('CACP','Cachecóis e pashminas'),
	    ('LENC','Lenços'),
	    ('BOLS','Bolsas'),
	    ('SAPT','Sapatos'),
	    ('MEIA','Meias')
	)

	grupo = models.CharField('Grupos', max_length=300, default='ACES', choices = GRUPOS)
	categoria = models.CharField('Categorias', max_length=300, default='CAMT', choices = CATEGORIAS)
	nome = models.CharField('Nome', max_length=50)
	modelo = models.CharField('Modelo', max_length=20)
	preco = models.DecimalField('Preço', max_digits=5, decimal_places=2)
	status = models.BooleanField('Disponível')

	def __str__(self):
		return self.nome + ' ' + self.modelo