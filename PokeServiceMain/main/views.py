import string
from django.http import JsonResponse
from django.shortcuts import render
from django.core.cache import cache
from django.core.paginator import Paginator 

import PokeServiceMain.forms as forms
import PokeServiceMain.casts as casts
import typing, re,  random, math
import main.models as models
import main.battle as battle


# Create your views here.
def PokemonsCatalog(request):

    LIMIT_OF_POKEMONS: int = 6
    if 'search' in request.GET:
        pat = rf".*{request.GET['search']}.*"
        pattern = re.compile(pat)
        pokemons_by_cached = [pokemon for pokemon in casts.GetPokemons() if pattern.match(pokemon)]
    else:
        pokemons_by_cached = cache.get('pokemons')

    if not pokemons_by_cached:
        pokemons_by_cached = casts.GetPokemons()
        cache.set('pokemons', pokemons_by_cached)

    catalog_paginator = Paginator(pokemons_by_cached, LIMIT_OF_POKEMONS)

    page = int(request.GET.get('page', 1))
    page_pokemons = catalog_paginator.get_page(page)


    # OFFSET_OF_LIMIT: int = (page - 1) * LIMIT_OF_POKEMONS
    if 'search' in request.GET:
        pokemons_data_by_cached = casts.GetPokemonsData(pokemons=page_pokemons.object_list)
    else:
        pokemons_data_by_cached = cache.get(f'pokemons_data{page}')
    if not pokemons_data_by_cached:
        pokemons_data_by_cached = casts.GetPokemonsData(pokemons=page_pokemons.object_list) # list of dicts
        cache.set(f'pokemons_data{page}', pokemons_data_by_cached, 3600)

    
    print(page_pokemons.object_list)

    data_2_page:dict = {
        'pokemons_data': pokemons_data_by_cached,
        'page_pokemons' : page_pokemons
        }
    return render(request, "main/catalog.html", data_2_page)



def PokemonDetail(request, pokemon: str = None):
    return render(request, 'main/detailed.html', {'pokemon_data': casts.GetPokemonData(pokemon)})


def PokemonBattle(request, pokemon: str = None):
    user_pokemon_data = casts.GetPokemonData(pokemon)
    
    #check if it start
    if request.method != 'POST':
        battle_form = forms.BattleForm()
        email_form = forms.EmailForm()
        battle_round: int = 0

        enemy_pokemon_data = casts.GetRandomPokemonData(exception_pokemons=[pokemon])

        user_pokemon_stats: typing.Dict[str,str] = battle.InitPokemonStats(user_pokemon_data)
        enemy_pokemon_stats: typing.Dict[str,str] = battle.InitPokemonStats(enemy_pokemon_data)
        
        logs: typing.List[str] = ['[LOG] Starting battle.... Lets fight!']
        
        battle.SyncSession(request, 
                           ['user_pokemon_stats', 'enemy_pokemon_stats', 'battle_round', 'logs', 'hitted_object'],
                           [user_pokemon_stats, enemy_pokemon_stats,  battle_round, logs, {'is_user': 'false', 'is_enemy': 'false'}])

    elif 'fastnsend' in request.POST:
        email_form = forms.EmailForm(request.POST)
        if email_form.is_valid():
            user_email = email_form.cleaned_data['email']
        else:
            user_email = ''

        user_pokemon_stats: typing.Dict[str,str] = request.session.get('user_pokemon_stats')
        enemy_pokemon_stats: typing.Dict[str,str] = request.session.get('enemy_pokemon_stats')
        battle_round = request.session.get('battle_round') + 1
        

        while user_pokemon_stats['hp'] > 0 and enemy_pokemon_stats['hp'] > 0:
            logs_of_battle: typing.List[str] = [f'[LOG] Round #{battle_round}']

            user_roll = random.randint(1, 10)
            logs_of_battle.append(f' | PC roll: {user_roll}')

            battle.AttackPart(request, user_roll, logs_of_battle, user_pokemon_stats, enemy_pokemon_stats)

            if user_pokemon_stats['hp'] <= 0 or enemy_pokemon_stats['hp'] <= 0:
                current_user_id = request.user.id
                if not current_user_id:
                    current_user_id = 'None'
                pokemon_winner = user_pokemon_stats if user_pokemon_stats['hp'] > 0 else enemy_pokemon_stats
                battle.SaveBattleResult(current_user_id, battle_round, user_pokemon_stats['name'], enemy_pokemon_stats['name'], pokemon_winner['name'])
                logs: typing.List[str] = request.session.get('logs')
                logs.append("".join(logs_of_battle))
                logs.append(f"[LOG] Battle end! Congratulation {pokemon_winner['name'].upper()}!")
                request.session['logs'] = logs
            
                data_2_render: dict = {
                    'winner': pokemon_winner,
                    'battle_round': battle_round,
                    'battle_logs': request.session.get('logs')
                }

                if user_email != '':
                    battle.SendBattleResult(to_email=user_email, 
                                            body='\n'.join(logs), 
                                            subject=f"[PokeService] Battle {user_pokemon_stats['name']} vs {enemy_pokemon_stats['name']}")

                return render(request, 'main/battle_end.html', data_2_render)
            
            logs: typing.List[str] = request.session.get('logs')
            logs.append("".join(logs_of_battle))

            battle_round+=1
            battle.SyncSession(request,
                               ['user_pokemon_stats', 'enemy_pokemon_stats', 'battle_round', 'logs'], 
                               [ user_pokemon_stats,  enemy_pokemon_stats, battle_round, logs])

    else:
        email_form = forms.EmailForm()
        battle_form = forms.BattleForm(request.POST)
        if battle_form.is_valid():
            battle_round = request.session.get('battle_round') + 1
            logs_of_battle: typing.List[str] = [f'[LOG] Round #{battle_round}']

            user_roll = battle_form.cleaned_data['user_roll']
            logs_of_battle.append(f' | User roll: {user_roll}')

            user_pokemon_stats: typing.Dict[str,str] = request.session.get('user_pokemon_stats')
            enemy_pokemon_stats: typing.Dict[str,str] = request.session.get('enemy_pokemon_stats')

            battle.AttackPart(request, user_roll, logs_of_battle, user_pokemon_stats, enemy_pokemon_stats)

            if user_pokemon_stats['hp'] <= 0 or enemy_pokemon_stats['hp'] <= 0:
                current_user_id = request.user.id
                if not current_user_id:
                    current_user_id = 'None'
                pokemon_winner = user_pokemon_stats if user_pokemon_stats['hp'] > 0 else enemy_pokemon_stats

                battle.SaveBattleResult(current_user_id, battle_round, user_pokemon_stats['name'], enemy_pokemon_stats['name'], pokemon_winner['name'])

                logs: typing.List[str] = request.session.get('logs')
                logs.append("".join(logs_of_battle))
                logs.append(f"[LOG] Battle end! Congratulation {pokemon_winner['name'].upper()}!")
                request.session['logs'] = logs


                data_2_render: dict = {
                    'winner': pokemon_winner,
                    'battle_round': battle_round,
                    'battle_logs': request.session.get('logs')
                }
                return render(request, 'main/battle_end.html', data_2_render)

            logs: typing.List[str] = request.session.get('logs')
            logs.append("".join(logs_of_battle))


            battle.SyncSession(request,
                               ['user_pokemon_stats', 'enemy_pokemon_stats', 'battle_round', 'logs'], 
                               [ user_pokemon_stats,  enemy_pokemon_stats, battle_round, logs])


    print( request.session.get('hitted_object'))
    data_2_render: dict = {
        'user_pokemon_stats': request.session.get('user_pokemon_stats'),
        'enemy_pokemon_stats': request.session.get('enemy_pokemon_stats'),
        'battle_form': battle_form,
        'email_form': email_form,
        'battle_round': battle_round,
        'battle_logs': request.session.get('logs'),
        'hitted_object': request.session.get('hitted_object')
    }
    return render(request, 'main/battle.html', data_2_render)


import requests


## ------------------------------- Login and Registered
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout, login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


@login_required(login_url='/login/')
def Profile(request):
    return render(request, 'main/profile.html')


def Logout(request):
    logout(request)
    return redirect('catalog')

def RegisterNewUser(request):
    if request.method == 'POST':
        form = forms.CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.backend = 'django.contrib.auth.backends.ModelBackend'
            login(request, user)
            return redirect('profile') 
    else:
        form = AuthenticationForm()

    return render(request, 'main/registration.html', {'form': form})

def LoginUser(request):
    form = None
    second_code = None
    if request.method == 'POST':
        form = forms.LoginUserForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            print(username)
            print(email)
            print(password)
            user = authenticate(request, username=username, password=password)
            print(user)
            if user:
                email_subject = "PokeService. Вход в свой профиль"
                second_code = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
                print('code_second:', second_code)
                email_message = "Ваш код для подтверждения, никому не сообщайте: {}.".format(second_code)
                battle.SendBattleResult(email_subject, email, email_message)
                request.session['user_email'] = email
                request.session['username'] = username
                request.session['password'] = password
                request.session['second_code'] = second_code
                next_url = request.GET.get('next', '')
                print(next_url)
                if next_url:
                    return redirect(next_url)
                else:
                    return redirect('profile')
    else:
        form = forms.LoginUserForm()
    return render(request, '../templates/registration/login.html', {'form': form})

from django.contrib import messages

def CodeConfirmView(request):
    if request.method == 'POST':
        form = forms.CodeConfirmForm(request.POST)
        if form.is_valid():
            second_code = request.session.get('second_code', None)
            email = request.session.get('user_email')
            username = request.session.get('username')
            password = request.session.get('password')
            user_entered_code = form.cleaned_data['code']
            print(email)
            print(username)
            print(password)
            user = authenticate(request, username=username, password=password)
            print(user)
            if user is not None:
                if user_entered_code == second_code:
                    login(request, user)
                    messages.success(request, 'Successfully logged in')
                    del request.session['second_code']
                    return redirect('profile')
                else:
                    messages.error(request, 'Invalid code')
    else:
        form =  forms.CodeConfirmForm()
    return render(request, 'main/code_confirmation.html', {'form': form})


## ------------------------------- APIv2


from rest_framework.views import APIView

#GET /api/v2/pokemon/list/?limit=12&offset=4&filter=name,hp,attack
class PokemonListApi2View(APIView):
    def get(self, request, format=None):
        limit = request.query_params.get('limit', 6)
        offset = request.query_params.get('offset', 0)
        filters = self.request.query_params.get('filter', [])
        
        data = casts.GetPokemons(n_pokemons=int(limit), offset_n=int(offset))
        filtered_data = casts.FilterPokemonData(data, filters)
        return JsonResponse(filtered_data, safe=False)

#GET /api/v2/pokemon/5?filter=name,hp,speed
class PokemonIdApi2View(APIView):
    def get(self, request, pokemon_id):
        filters = request.query_params.get('filter', [])
        data = requests.get(casts.URL_2_CAST+f"/{pokemon_id}").json()
        filtered_data = casts.FilterPokemonData([data['name']], filters)
        return JsonResponse(filtered_data, safe=False)

#GET /api/v2/pokemon/random
class PokemonRandomIdApi2View(APIView):
    def get(self, request):
        pokemon = casts.GetRandomPokemonData()
        return JsonResponse(pokemon, safe=False)
    
#GET /api/v2/battle/fast?user_id=4&enemy_id=2
class PokemonBattleFastApi2View(APIView):
    def get(self, request):
        user_pokemon = request.query_params.get('user_id', 0)
        enemy_pokemon = request.query_params.get('enemy_id', None)
        if not enemy_pokemon:
            enemy_pokemon = casts.GetRandomPokemonData()["id"]
        return JsonResponse(battle.GetResultFastBattle(user_pokemon, enemy_pokemon), safe=False)

#GET /api/v2/battle?user_id=4&enemy_id=2
class PokemonBattleInfoApi2View(APIView):
    def get(self, request):
        user_pokemon = request.query_params.get('user_id', 0)
        enemy_pokemon = request.query_params.get('enemy_id', None)
        if not enemy_pokemon:
            enemy_pokemon = casts.GetRandomPokemonData()["id"]
        battle_info = {
            "pokemon1": casts.GetPokemonData(user_pokemon),
            "pokemon2": casts.GetPokemonData(enemy_pokemon)
        }
        return JsonResponse(battle_info, safe=False)

from main.serializers import SerializerBattleLog

class PokemonBattleLogRoundApi2View(APIView):
    def post(self, request, format=None):
        serializer = SerializerBattleLog(data=request.data)
        # TODO

## ------------------------------ FTP


def PokemonSave2FTP(request, pokemon):
    try:
        casts.SavePokemon2FTP(pokemon)
        return JsonResponse({"status": "success"})
    except:
        return JsonResponse({"status": "failed"})
    

def PokemonsDashboards(request):
    return render(request, 'main/dashboards.html')
