from django.test import TestCase
from django.urls import reverse

# Create your tests here.
from django.urls import include, path, reverse
from rest_framework import status
from rest_framework.test import APITestCase, URLPatternsTestCase
import json

class PokemonsTests(APITestCase):
    def test_PokemonList(self):
        url = '/api/v2/pokemon/list?limit=1&offset=4&filter=name,hp,attack'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content), [{"name": "charmeleon", "hp": 58, "attack": 64}])

    def test_GetPokemonById(self):
        url = '/api/v2/pokemon/5?filter=name,hp,speed'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_GetRandomPokemon(self):
        url = '/api/v2/pokemon/random'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertNotEqual(json.loads(response.content), None)

    def test_FastBattle(self):
        url = '/api/v2/battle/fast?user_id=4&enemy_id=2'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn(json.loads(response.content)["user_pokemon"], ["charmander", "ivysaur"])

    def SavePokemonToFTP(self):
        url = '/api/v1/save/5'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content), {"status": "success"})

    def test_BattleInfo(self):
        url = '/api/v2/battle?user_id=4&enemy_id=2'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        equals_data = ["charmander", "ivysaur"]
        self.assertIn(json.loads(response.content)["pokemon1"]["name"], equals_data)
        self.assertIn(json.loads(response.content)["pokemon2"]["name"], equals_data)


