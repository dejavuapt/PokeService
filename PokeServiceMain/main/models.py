from django.db import models
from django.contrib.auth.models import User,  AbstractBaseUser


#d
# Create your models here.
class BattleLog(models.Model):
    account_id = models.CharField(max_length=30, default='None')
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


class BaseUser(AbstractBaseUser):
    email = models.EmailField(unique=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email