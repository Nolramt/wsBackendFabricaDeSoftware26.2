from rest_framework import serializers
from ..models import PersonagemFav, LocalizacaoFav, EpisodioFav

class PersonagemSerializers(serializers.Serializer):

    id = serializers.IntegerField()
    name = serializers.CharField()
    status = serializers.CharField()
    species = serializers.CharField()
    type = serializers.CharField(allow_blank=True)
    gender = serializers.CharField()
    image = serializers.URLField()
    episode = serializers.ListField()

class LocalizacaoSerializers(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    type =  serializers.CharField()
    dimension = serializers.CharField()
    residents = serializers.ListField(allow_empty=True)

class EpisodioSerializers(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    air_date = serializers.CharField()
    episode = serializers.CharField()
    characters = serializers.ListField()
    url = serializers.CharField()

class PersonagemFavSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonagemFav
        fields = "__all__"


class LocalizacaoFavSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocalizacaoFav
        fields = "__all__"


class EpisodioFavSerializer(serializers.ModelSerializer):
    class Meta:
        model = EpisodioFav
        fields = "__all__"