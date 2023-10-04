from django.http import HttpResponse
from django.shortcuts import render

import requests as rqts;

POKE_API_URL:str = "https://pokeapi.co/api/v2/";
 
def index(request):

    
    
    count_of_all_pokemons = str(rqts.get(POKE_API_URL + "pokemon/").json()['count']);
    response2pokeapi = rqts.get(POKE_API_URL + "pokemon?limit=" + str(count_of_all_pokemons));

    pokemons_data = response2pokeapi.json();

    data2render = {"pokemons": pokemons_data['results']};

    return render(request, "index.html", data2render)


def search(request):
    return render(request, "search.html")

def SearchPokemon(request):
    pokename = request.POST.get("search", 'null');
    

    if(pokename != 'null'):
        poke_url = POKE_API_URL + f"pokemon/{pokename.lower()}/";
        response2pokeapi = rqts.get(poke_url);
        if(response2pokeapi.status_code == 200):
            pokemons_data = response2pokeapi.json();
            data2render = {"pokemons": pokemons_data['forms']};
        else:
            data2render = {}
    else:
        data2render = {}

    return render(request, 'index.html', data2render);