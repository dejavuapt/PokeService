from django.db import models

# Create your models here.
class BattleLog(models.Model):
    battle_date = models.DateTimeField()
    battle_round = models.IntegerField()
    user_pokemon = models.CharField(max_length=30)
    enemy_pokemon = models.CharField(max_length=30)
    battle_round_winner = models.CharField(max_length=30)