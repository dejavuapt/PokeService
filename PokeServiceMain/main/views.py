from django.shortcuts import render
from django.core.cache import cache
from django.core.paginator import Paginator 


import PokeServiceMain.casts as casts
import typing, re



# Create your views here.
def PokemonsCatalog(request):
    

    LIMIT_OF_POKEMONS: int = 6
    if 'search' in request.GET:
        pat = rf".*{request.GET['search']}.*"
        pattern = re.compile(pat)
        pokemons_by_cached = [pokemon for pokemon in casts.GetPokemons() if pattern.match(pokemon)]
    else:
        pokemons_by_cached = cache.get('pokemons')

    if not pokemons_by_cached:
        pokemons_by_cached = casts.GetPokemons()
        cache.set('pokemons', pokemons_by_cached)

    catalog_paginator = Paginator(pokemons_by_cached, LIMIT_OF_POKEMONS)

    page = int(request.GET.get('page', 1))
    page_pokemons = catalog_paginator.get_page(page)


    # OFFSET_OF_LIMIT: int = (page - 1) * LIMIT_OF_POKEMONS
    if 'search' in request.GET:
        pokemons_data_by_cached = casts.GetPokemonsData(pokemons=page_pokemons.object_list)
    else:
        pokemons_data_by_cached = cache.get(f'pokemons_data{page}')
    if not pokemons_data_by_cached:
        pokemons_data_by_cached = casts.GetPokemonsData(pokemons=page_pokemons.object_list) # list of dicts
        cache.set(f'pokemons_data{page}', pokemons_data_by_cached, 3600)

    
    print(page_pokemons.object_list)

    data_2_page:dict = {
        'pokemons_data': pokemons_data_by_cached,
        'page_pokemons' : page_pokemons
        }
    return render(request, "main/catalog.html", data_2_page)



def PokemonDetail(request, pokemon: str = None):
    return render(request, 'main/detailed.html', {'pokemon_data': casts.GetPokemonData(pokemon)})
