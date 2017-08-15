#coding:utf-8

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    context_dict = {}
    bold_message = 'E aí, BSI, tudo em cima?'
    autor = 'Marco André Mendes'
    context_dict['bold_message'] = bold_message
    context_dict['autor'] = autor

    return render(request, 'rango/index.html', context_dict)

def about(request):
    pagina = '''
    <strong>Sobre o Rango</strong> </br>

    <a href='/rango/'>Home</a>
    '''
    return HttpResponse(pagina)
