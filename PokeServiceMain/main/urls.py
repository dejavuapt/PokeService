from django.urls import path
from . import views as main_views

urlpatterns = [
    path('', main_views.PokemonsCatalog, name='catalog'),
    path('pokemon/<pokemon>', main_views.PokemonDetail, name='pokemon_detail'),
    path('battle/<pokemon>', main_views.PokemonBattle, name='battle'),

    path('api/v1/pokemon/list/', main_views.PokemonListApiView.as_view(), name="pokemon-list"),
    path('api/v1/pokemon/<int:pokemon_id>', main_views.PokemonIdApiView.as_view(), name="pokemon-id"),
    path('api/v1/pokemon/random', main_views.PokemonRandomIdApiView.as_view(), name="pokemon-random"),
    # path('api/v1/fight', main_views.PokemonBattlePlayersApiView.as_view(), name="pokemon-battle"),
    # path('api/v1/fight/<int:roll>/', main_views.PokemonBattlePlayersApiView.as_view(), name="pokemon-battle-roll"),
    path('api/v1/fight/fast', main_views.PokemonBattleFastApiView.as_view(), name="pokemon-battle-fast" ),


    path('api/v1/save/<pokemon>', main_views.PokemonSave2FTP, name="pokemon-save")
]
