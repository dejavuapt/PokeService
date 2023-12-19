from django.urls import path, include, re_path
from . import views as main_views
from django.contrib.auth import views as auth_views




urlpatterns = [
    path('', main_views.PokemonsCatalog, name='catalog'),
    path('pokemon/<pokemon>', main_views.PokemonDetail, name='pokemon_detail'),
    path('battle/<pokemon>', main_views.PokemonBattle, name='battle'),
    path('dashboards/', main_views.PokemonsDashboards, name='dashboards'),

    path('api/v2/pokemon/list', main_views.PokemonListApi2View.as_view(), name="pokemon-listv2"),
    path('api/v2/pokemon/<int:pokemon_id>', main_views.PokemonIdApi2View.as_view(), name="pokemon-idv2"),
    path('api/v2/pokemon/random', main_views.PokemonRandomIdApi2View.as_view(), name="pokemon-randomv2"),
    path('api/v2/battle', main_views.PokemonBattleInfoApi2View.as_view(), name="pokemon-battle"),
    # path('api/v1/fight/<int:roll>/', main_views.PokemonBattlePlayersApiView.as_view(), name="pokemon-battle-roll"),
    path('api/v2/battle/fast', main_views.PokemonBattleFastApi2View.as_view(), name="pokemon-battle-fastv2" ),

    path('api/v1/save/<pokemon>', main_views.PokemonSave2FTP, name="pokemon-save"),


    path('profile/', main_views.Profile, name="profile"),
    path('login/', main_views.LoginUser, name="login"),
    path('code-confirmation/', main_views.CodeConfirmView, name="code_confirmation"),
    path('logout/', main_views.Logout, name="logout"),
    path('registration/', main_views.RegisterNewUser, name="register"),


    path('reset_password/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('reset_password/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
