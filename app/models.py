from django.db import models

# Create your models here.

class PersonagemFav(models.Model):
    id_externo = models.IntegerField(unique=True)
    name = models.CharField(max_length=254)
    status = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    type = models.CharField(max_length=100, blank=True)
    gender = models.CharField(max_length=50)
    image = models.URLField()
    pasta = models.CharField(max_length=100, blank=True, default="Geral")

    def __str__(self):
        return self.name
class LocalizacaoFav(models.Model):
    id_externo = models.IntegerField(unique=True)
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=100)
    dimension = models.CharField(max_length=255)
    pasta = models.CharField(max_length=100, blank=True, default="Geral")

    def __str__(self):
        return self.name


class EpisodioFav(models.Model):
    id_externo = models.IntegerField(unique=True)
    name = models.CharField(max_length=255)
    air_date = models.CharField(max_length=100)
    episode = models.CharField(max_length=50)
    pasta = models.CharField(max_length=100, blank=True, default="Geral")

    def __str__(self):
        return self.name