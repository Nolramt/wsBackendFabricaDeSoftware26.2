from django.db import models

# Create your models here.

class PastaFavoritos(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
    
class PersonagemFav(models.Model):
    id_externo = models.IntegerField(unique=True)
    name = models.CharField(max_length=254)
    status = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    type = models.CharField(max_length=100, blank=True)
    gender = models.CharField(max_length=50)
    image = models.URLField()
    pasta = models.ForeignKey(
        PastaFavoritos, on_delete=models.SET_NULL, null=True, blank=True, related_name="personagens"
    )

    def __str__(self):
        return self.name
class LocalizacaoFav(models.Model):
    id_externo = models.IntegerField(unique=True)
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=100)
    dimension = models.CharField(max_length=255)
    pasta = models.ForeignKey(
        PastaFavoritos, on_delete=models.SET_NULL, null=True, blank=True, related_name="localizacoes"
    )

    def __str__(self):
        return self.name


class EpisodioFav(models.Model):
    id_externo = models.IntegerField(unique=True)
    name = models.CharField(max_length=255)
    air_date = models.CharField(max_length=100)
    episode = models.CharField(max_length=50)
    pasta = models.ForeignKey(
        PastaFavoritos, on_delete=models.SET_NULL, null=True, blank=True, related_name="episodios"
    )

    def __str__(self):
        return self.name
