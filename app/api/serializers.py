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

