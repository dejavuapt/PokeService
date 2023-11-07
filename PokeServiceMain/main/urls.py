from django.urls import path
from . import views as main_views

urlpatterns = [
    path('', main_views.PokemonsCatalog, name='catalog'),
    path('pokemon/<pokemon>', main_views.PokemonDetail, name='pokemon_detail')
]
