from django.db import models

# Create your models here.
class BattleLog(models.Model):
    battle_date = models.DateTimeField()
    battle_round = models.IntegerField()
    user_pokemon = models.CharField(max_length=30)
    enemy_pokemon = models.CharField(max_length=30)
    battle_round_winner = models.CharField(max_length=30)


class BattleRound(models.Model):
    first_pokemon_id = models.IntegerField()
    second_pokemon_id = models.IntegerField()
    first_pokemon_hp = models.IntegerField()
    second_pokemon_hp = models.IntegerField()
    first_pokemon_roll = models.IntegerField()
    second_pokemon_roll = models.IntegerField()
    round_number = models.IntegerField()
    winner_id = models.IntegerField()
    is_last = models.BooleanField()


