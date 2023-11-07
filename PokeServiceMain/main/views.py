from django.shortcuts import render
import PokeServiceMain.casts as casts

# Create your views here.
def PokemonsCatalog(request):
    # print(casts.GetAllPokemons())
    return render(request, "main/catalog.html")