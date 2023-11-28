from django.db import models

# Create your models here.
class BattleLog(models.Model):
    battle_date = models.DateTimeField()
    battle_round = models.IntegerField()
    user_pokemon = models.CharField(max_length=30)
    enemy_pokemon = models.CharField(max_length=30)
    battle_round_winner = models.CharField(max_length=30)


class Pokemon(models.Model):
    name = models.CharField(max_length=30)
    poke_id = models.IntegerField()
    picture_url = models.CharField(max_length=200)
    back_picture_url = models.CharField(max_length=200)
    height = models.IntegerField()
    weight = models.IntegerField()
    hp = models.IntegerField()
    attack = models.IntegerField()
    defense = models.IntegerField()
    speed = models.IntegerField()
    types_of_attack = models.CharField(max_length=200)



