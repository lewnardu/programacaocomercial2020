from django.contrib import admin
from django.urls import path
from estoque.views import Autenticacao

urlpatterns = [
    path('', Autenticacao.as_view(), name='index'),
]
