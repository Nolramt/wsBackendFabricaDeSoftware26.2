import requests
from .serializers import PersonagemSerializers, LocalizacaoSerializers, EpisodioSerializers
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

class PersonagemViewsets(viewsets.ViewSet):
    def list(self, request):
        try:
            resposta = requests.get(
                "https://rickandmortyapi.com/api/character",
            )
            if resposta.status_code != 200:
                return Response(
                    {
                        "erro": "Erro ao consultar API externa."
                    },
                    status=status.HTTP_502_BAD_GATEWAY
                )
            dados = resposta.json()

            serializer = PersonagemSerializers(
                data=dados["results"],
                many=True
            )
            serializer.is_valid(
                raise_exception=True
            )
            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )
        except requests.exceptions.RequestException:

            return Response(
                {
                    "erro": "Não foi possível acessar a API externa."
                },
                status=status.HTTP_503_SERVICE_UNAVAILABLE
            )
class LocalizacaoViewsets(viewsets.ViewSet):
    def list(self, request):
        try:
            resposta = requests.get(
                "https://rickandmortyapi.com/api/location"
            )
            if resposta.status_code != 200:
                return Response({
                    "erro": "Erro ao consultar API externa."
                },
                status=status.HTTP_502_BAD_GATEWAY
                )
            dados = resposta.json()

            serializer = LocalizacaoSerializers(
                data=dados["results"],
                many=True
            )
            serializer.is_valid(
                raise_exception=True
            )
            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )

        except requests.exceptions.RequestException:

            return Response(
                {
                    "erro": "Não foi possível acessar a API externa."
                },
                status=status.HTTP_503_SERVICE_UNAVAILABLE
            )

class EpisodioViewsets(viewsets.ViewSet):
    def list(self, request):
        try:
            resposta = requests.get(
                "https://rickandmortyapi.com/api/episode"
            )
            if resposta.status_code != 200:
                return Response({
                    "erro": "Erro ao consultar API externa."
                },
                status=status.HTTP_502_BAD_GATEWAY
                )
            dados = resposta.json()

            serializer = EpisodioSerializers(
                data=dados["results"],
                many=True
            )
            serializer.is_valid(
                raise_exception=True
            )
            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )

        except requests.exceptions.RequestException:

            return Response(
                {
                    "erro": "Não foi possível acessar a API externa."
                },
                status=status.HTTP_503_SERVICE_UNAVAILABLE
            )