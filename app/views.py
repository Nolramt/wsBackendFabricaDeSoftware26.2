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
                erro = "Nenhuma localização encontrada com esse nome."

        except requests.exceptions.RequestException:
            erro = "Não foi possível acessar a API externa."

    return render(request, 'localizacao.html', {
        'info': info,
        'erro': erro,
        'nome': nome,
    })

def buscarEpisodioViews(request):
    nome = (request.GET.get('nome'))

    info = None
    erro = None

    if (nome):
        try:
            resposta = requests.get(f"https://rickandmortyapi.com/api/episode", params={"name": nome})

            if resposta.status_code == 200:
                info = resposta.json().get("results", [])
            else:
                erro = "Nenhum episodio encontrado com esse nome."

        except requests.exceptions.RequestException:
            erro = "Não foi possível acessar a API externa."

    return render(request, 'episodio.html', {
        'info': info,
        'erro': erro,
        'nome': nome,
    })

