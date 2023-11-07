from django.shortcuts import render
from django.core.cache import cache

import PokeServiceMain.casts as casts

import pagination

# Create your views here.
def PokemonsCatalog(request):
    # LIMIT_OF_POKEMONS: int = 12
    pokemons_by_cached = cache.get('pokemons_data')
    if not pokemons_by_cached:
        pokemons_by_cached = casts.GetPokemonsData(6) # list of dicts
        cache.set('pokemons_data', pokemons_by_cached, 3600)

    data_2_page:dict = {'pokemons_data': pokemons_by_cached}
    return render(request, "main/catalog.html", data_2_page)