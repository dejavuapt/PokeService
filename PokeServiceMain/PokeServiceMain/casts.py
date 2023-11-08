import requests
import typing 
import random
from ftplib import FTP
import PokeServiceMain.settings as settings
import datetime, io

URL_2_CAST: str = "https://pokeapi.co/api/v2/pokemon"


def GetPokemons(n_pokemons: int = None, offset_n: int = 0) -> typing.List[str]: 
    try:
        if n_pokemons == None:
            count_of_pokemons = requests.get(URL_2_CAST).json()['count']
        else:
            count_of_pokemons = f'{n_pokemons}'
        response = requests.get(URL_2_CAST, params={"limit": count_of_pokemons, "offset": offset_n})
        data_of_response = response.json()
        return [pokemon['name'] for pokemon in data_of_response['results']]
    except requests.exceptions.HTTPError as http_error:
        return []
    

def GetPokemonData(pokemon: str) -> typing.Dict[str, str]:
    try:
        data_of_response = requests.get(URL_2_CAST + f'/{pokemon}').json()
        return {
            'name' : data_of_response['name'],
            'id':data_of_response['id'],
            'picture' : data_of_response['sprites']['front_default'], #
            'back_picture': data_of_response['sprites']['back_default'],
            'height' : data_of_response['height'],
            'weight' : data_of_response['weight'],
            'hp': data_of_response['stats'][0]['base_stat'],
            'attack': data_of_response['stats'][1]['base_stat'],
            'defense': data_of_response['stats'][2]['base_stat'],
            'speed': data_of_response['stats'][5]['base_stat'],
            'types_of_attack': ', '.join([data_of_response['types'][n]['type']['name'] for n in range(len(data_of_response['types']))])
        }
    except requests.exceptions.HTTPError as http_error:
        print(http_error)
        return {}
    
def GetPokemonsData(n_pokemons: int = None, offset_n: int = 0, pokemons: typing.List[str] = None) -> typing.List[dict]:
    try:
        if(pokemons == None and n_pokemons != None ):
            _pokemons = GetPokemons(n_pokemons, offset_n)
        else:
            _pokemons = pokemons

        return [GetPokemonData(pokemon) for pokemon in _pokemons]
        
    except requests.exceptions.HTTPError as http_error:
        return []

def GetRandomPokemonData(exception_pokemons: typing.List[str] = []) -> typing.Dict[str, str]:
    return GetPokemonData(random.choice([pokemon for pokemon in GetPokemons() if pokemon not in exception_pokemons]))


def FilterPokemonData(pokemons, filter):
    if filter != []:
        filter = filter.split(',')
        filter.insert(0,'name')

        filtered_pokemons_data = []
        for pokemon in pokemons:
            pokemon_data = GetPokemonData(pokemon)                
            filtered_pokemons_data.append({key: pokemon_data[key] for key in filter if key in pokemon_data})
        return filtered_pokemons_data
    else:
        return GetPokemonsData(pokemons=pokemons)
    

def SavePokemon2FTP(pokemon):
    pokemon_data = GetPokemonData(pokemon)
    today_folder = str(datetime.date.today()).replace('-','').strip()
    pokemon_md = f"---\n# Pokemon: {pokemon_data['name'].upper()}\n\n![source]({pokemon_data['picture']}\n---\n### Stats:\n-hp: {pokemon_data['hp']}\n-attack: {pokemon_data['attack']}\n "
    byted_pokemon_md = pokemon_md.encode('utf-8')

    with FTP(settings.FTP_HOST, settings.FTP_USER, settings.FTP_PASS) as ftp_connect:
        files = ftp_connect.nlst()
        if today_folder not in files:
            ftp_connect.mkd(today_folder)
        ftp_connect.cwd(today_folder)
        ftp_connect.storbinary(f"STOR {pokemon_data['name'].upper()}.md", io.BytesIO(byted_pokemon_md))
        ftp_connect.quit()