from django.shortcuts import render
from django.core.cache import cache
from django.core.paginator import Paginator 


import PokeServiceMain.casts as casts


# Create your views here.
def PokemonsCatalog(request):
    LIMIT_OF_POKEMONS: int = 6
    pokemons_by_cached = cache.get('pokemons')
    if not pokemons_by_cached:
        pokemons_by_cached = casts.GetPokemons()
        cache.set('pokemons', pokemons_by_cached)
    catalog_paginator = Paginator(pokemons_by_cached, LIMIT_OF_POKEMONS)

    page = int(request.GET.get('page', 1))

    OFFSET_OF_LIMIT: int = (page - 1) * LIMIT_OF_POKEMONS
    pokemons_data_by_cached = cache.get(f'pokemons_data{page}')
    if not pokemons_data_by_cached:
        pokemons_data_by_cached = casts.GetPokemonsData(LIMIT_OF_POKEMONS, OFFSET_OF_LIMIT) # list of dicts
        cache.set(f'pokemons_data{page}', pokemons_data_by_cached, 3600)

    
    page_pokemons = catalog_paginator.get_page(page)
    
    data_2_page:dict = {
        'pokemons_data': pokemons_data_by_cached,
        'page_pokemons' : page_pokemons
        }
    return render(request, "main/catalog.html", data_2_page)