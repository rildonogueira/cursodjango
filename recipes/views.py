from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'recipes/home.html', context={
        'name': 'Rildo',
        'idade': '12',
        'cpf': '152.158.300-45',
    })


def contato(request):
    return render(request, 'temp/temp.html')


def sobre(request):
    return HttpResponse('sobre')


def compra(request):
    return HttpResponse('compra')


def venda(request):
    return HttpResponse('vena')


def troca(request):
    return HttpResponse('troca')
