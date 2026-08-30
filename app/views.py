from django.shortcuts import render, redirect
import requests
from .models import PersonagemFav, LocalizacaoFav, EpisodioFav, PastaFavoritos
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

def favoritar_personagem(request):
    if request.method == "POST":
        nome_pasta = request.POST.get("pasta", "Geral")
        pasta, _ = PastaFavoritos.objects.get_or_create(nome=nome_pasta)

        PersonagemFav.objects.get_or_create(
            id_externo=request.POST.get("id_externo"),
            defaults={
                "name": request.POST.get("name"),
                "status": request.POST.get("status"),
                "species": request.POST.get("species"),
                "type": request.POST.get("type", ""),
                "gender": request.POST.get("gender"),
                "image": request.POST.get("image"),
                "pasta": pasta,
            }
        )
    return redirect(request.META.get("HTTP_REFERER", "/personagem/"))

def favoritar_localizacao(request):
    if request.method == "POST":
        nome_pasta = request.POST.get("pasta", "Geral")
        pasta, _ = PastaFavoritos.objects.get_or_create(nome=nome_pasta)
        
        LocalizacaoFav.objects.get_or_create(
            id_externo=request.POST.get("id_externo"),
            defaults={
                "name": request.POST.get("name"),
                "type": request.POST.get("type"),
                "dimension": request.POST.get("dimension"),
                "pasta": pasta,
            }
        )
    return redirect(request.META.get("HTTP_REFERER", "/localizacao/"))

def favoritar_episodio(request):
    if request.method == "POST":
        nome_pasta = request.POST.get("pasta", "Geral")
        pasta, _ = PastaFavoritos.objects.get_or_create(nome=nome_pasta)

        EpisodioFav.objects.get_or_create(
            id_externo=request.POST.get("id_externo"),
            defaults={
                "name": request.POST.get("name"),
                "air_date": request.POST.get("air_date"),
                "episode": request.POST.get("episode"),
                "pasta": pasta,
            }
        )
    return redirect(request.META.get("HTTP_REFERER", "/episodio/"))

