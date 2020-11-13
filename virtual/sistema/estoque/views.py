from django.views.generic import View
from django.shortcuts import render

class  Autenticacao(View):
	"""docstring for  Autenticacao"""
	
	def get(self, request):
		contexto = {
			'usuario':'',
			'senha': ''
		}
		return render(request, 'registration/login.html', contexto)