import requests
import typing 

URL_2_CAST: str = "https://pokeapi.co/api/v2/pokemon"


def GetAllPokemons() -> typing.List[str]: 
    count_of_pokemons = requests.get(URL_2_CAST).json()['count']
    try:
        response = requests.get(URL_2_CAST, params={"limit": count_of_pokemons, "offset": 0})
        data_of_response = response.json()
        return [pokemon['name'] for pokemon in data_of_response['results']]
    except requests.exceptions.HTTPError as http_error:
        return []

