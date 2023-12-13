from rest_framework import serializers
from main.models import BattleLog


class SerializerBattleLog(serializers.ModelSerializer):
    class Meta:
        model = BattleLog
        fields = ['first_pokemon_id',
                  'second_pokemon_id',
                  'first_pokemon_roll']


