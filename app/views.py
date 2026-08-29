from django.shortcuts import render
import requests

# Create your views here.

def buscarPersoViews(request):
    nome = (request.GET.get('nome'))

    info = None
    erro = None

    if (nome):
        try:
            resposta = requests.get(f"https://rickandmortyapi.com/api/character", params={"name": nome})

            if resposta.status_code == 200:
                info = resposta.json().get("results", [])
            else:
                erro = "Nenhum personagem encontrado com esse nome."

        except requests.exceptions.RequestException:
            erro = "Não foi possível acessar a API externa."

    return render(request, 'perso.html', {
        'info': info,
        'erro': erro,
        'nome': nome,
    })
def buscarLocalizacaoViews(request):
    nome = (request.GET.get('nome'))

    info = None
    erro = None

    if (nome):
        try:
            resposta = requests.get(f"https://rickandmortyapi.com/api/location", params={"name": nome})

            if resposta.status_code == 200:
                info = resposta.json().get("results", [])
            else:
                erro = "Nenhum personagem encontrado com esse nome."

        except requests.exceptions.RequestException:
            erro = "Não foi possível acessar a API externa."

    return render(request, 'perso.html', {
        'info': info,
        'erro': erro,
        'nome': nome,
    })


