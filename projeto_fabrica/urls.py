"""
URL configuration for projeto_fabrica project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from app.api.viewsets import PersonagemViewsets, LocalizacaoViewsets, EpisodioViewsets, PersonagemFavViewSet, LocalizacaoFavViewSet, EpisodioFavViewSet


from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

from rest_framework import routers

from app.views import buscarPersoViews, buscarLocalizacaoViews, buscarEpisodioViews

from app.views import favoritar_personagem, favoritar_localizacao, favoritar_episodio

routers = routers.DefaultRouter()
routers.register('personagens', PersonagemViewsets, basename="personagens")
routers.register('localizacao', LocalizacaoViewsets, basename="localizacao")
routers.register('episodio', EpisodioViewsets, basename="episodio")

routers.register('favoritos/personagem', PersonagemFavViewSet, basename="favoritos-personagem")
routers.register('favoritos/localizacao', LocalizacaoFavViewSet, basename="favoritos-localizacao")
routers.register('favoritos/episodio', EpisodioFavViewSet, basename="favoritos-episodio")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

    path('buscar/', include(routers.urls)),
    path('personagem/', buscarPersoViews),
    path('localizacao/', buscarLocalizacaoViews),
    path('episodio/', buscarEpisodioViews),
    path('favoritar-personagem/', favoritar_personagem, name='favoritar-personagem'),
    path('favoritar-localizacao/', favoritar_localizacao, name='favoritar-localizacao'),
    path('favoritar-episodio/', favoritar_episodio, name='favoritar-episodio'),
]
