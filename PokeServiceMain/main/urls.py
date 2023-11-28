from django.urls import path
from . import views as main_views

urlpatterns = [
    path('', main_views.PokemonsCatalog, name='catalog'),
    path('pokemon/<pokemon>', main_views.PokemonDetail, name='pokemon_detail'),
    path('battle/<pokemon>', main_views.PokemonBattle, name='battle'),

    path('api/v2/pokemon/list', main_views.PokemonListApi2View.as_view(), name="pokemon-listv2"),
    path('api/v2/pokemon/<int:pokemon_id>', main_views.PokemonIdApi2View.as_view(), name="pokemon-idv2"),
    path('api/v2/pokemon/random', main_views.PokemonRandomIdApi2View.as_view(), name="pokemon-randomv2"),
    # path('api/v1/fight', main_views.PokemonBattlePlayersApiView.as_view(), name="pokemon-battle"),
    # path('api/v1/fight/<int:roll>/', main_views.PokemonBattlePlayersApiView.as_view(), name="pokemon-battle-roll"),
    path('api/v2/battle/fast', main_views.PokemonBattleFastApi2View.as_view(), name="pokemon-battle-fastv2" ),


    path('api/v1/save/<pokemon>', main_views.PokemonSave2FTP, name="pokemon-save")
]
