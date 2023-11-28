from rest_framework import serializers
from main.models import Pokemon


class PokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemon
        fields = ['name', 'poke_id', 'picture_url', 'back_picture_url',
                  'height', 'weight', 'hp', 'attack', 'defense', 'speed',
                  'types_of_attack']


