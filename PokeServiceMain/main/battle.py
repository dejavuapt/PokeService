import typing, datetime, random, math
import main.models as models
from email.message import EmailMessage
from email.mime.text import MIMEText
import ssl, smtplib 
import PokeServiceMain.settings as main_settings


def InitPokemonStats(pokemon_data: typing.Dict[str,str]) -> typing.Dict[str,str]:
    return {
            'name': pokemon_data['name'],
            'hp': pokemon_data['hp'],
            'back_picture': pokemon_data['back_picture'],
            'picture':pokemon_data['picture'],
            'full_hp': pokemon_data['hp'],
            'attack': pokemon_data['attack'],
            'defense': pokemon_data['defense']
            }


def SyncSession(request, params, values) -> None:
    try:
        for param, value in zip(params, values):
            request.session[param] = value
    except IndexError as ie:
        pass 



def SaveBattleResult(round: int, user_pok:str , enemy_pok:str, winner_pok:str) -> None:
    battle_result = models.BattleLog(
                    battle_date = datetime.datetime.now(),
                    battle_round = round,
                    user_pokemon = user_pok,
                    enemy_pokemon = enemy_pok,
                    battle_round_winner = winner_pok
                )
    battle_result.save()


def AttackPart(request, user_roll: int, logs_of_battle: typing.List[str], user_stats, enemy_stats) -> None:
    enemy_roll = random.randint(1, 10)
    logs_of_battle.append(f' | PC roll: {enemy_roll}')

    if user_roll % 2 == enemy_roll % 2:
        attack_value: int = math.floor(user_stats['attack']*(enemy_stats['defense']/100))
        enemy_stats['hp'] -= attack_value
        logs_of_battle.append(f" | {user_stats['name'].upper()} attacked {enemy_stats['name'].upper()} by {attack_value}")
        request.session['hitted_object'] = {'is_user': 'false', 'is_enemy': 'true'}
    else:
        attack_value: int = math.floor(enemy_stats['attack']*(user_stats['defense']/100))
        user_stats['hp'] -= attack_value
        logs_of_battle.append(f" | {enemy_stats['name'].upper()} attacked {user_stats['name'].upper()} by {attack_value}")
        request.session['hitted_object'] = {'is_user': 'true', 'is_enemy': 'false'}


def SendBattleResult(subject:str, to_email:str, body: str):
    email_message = MIMEText(body)
    email_message['From'] = main_settings.EMAIL
    email_message['To'] = to_email
    email_message['Subject'] = subject

    try:
        smtp = smtplib.SMTP('smtp.mail.ru', 587)
        smtp.starttls()
        smtp.login(main_settings.EMAIL, main_settings.EMAIL_PASSWORD)
        smtp.sendmail(main_settings.EMAIL, to_email, email_message.as_string())
        smtp.quit()
    except AttributeError as ae:
        print('Exception because email and email_password didnt set in main.settings.py. Please check README to set')
        return