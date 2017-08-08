#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    pagina = '''
    <strong>Rango</strong> diz olá pra galera!</br>
    <a href='/rango/about/'>About</a>
    '''
    return HttpResponse(pagina)

def about(request):
    pagina = '''
    <strong>Sobre o Rango</strong> </br>

    <a href='/rango/'>Home</a>
    '''
    return HttpResponse(pagina)
