from rest_framework import serializers

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
