from django.shortcuts import render
import random
import requests

# Create your views here.

def error_404_view(request, exception):
    return render(request, "error_page.html")

def index(request):
    random_number = random.randint(1, 7527)
    url = f"https://api.disneyapi.dev/characters/{random_number}"
    r = requests.get(url)
    if r.status_code == 200:
        res = r.json()
        character = {
            'id' : res['_id'],
            'img_url' : res['imageUrl'],
            'films' : f"{[film for film in res['films']] if len(res['films']) > 0 else 'Not available'}",
            'shortfilms' : f"{[shortFilms for shortFilms in res['shortFilms']] if len(res['shortFilms']) > 0 else 'Not available'}",
            'tvshows' : f"{[tvShows for tvShows in res['tvShows']] if len(res['tvShows']) > 0 else 'Not available'}",
            'videogames' : f"{[videoGames for videoGames in res['videoGames']] if len(res['videoGames']) > 0 else 'Not available'}",
            'parkattractions' : f"{[parkAttractions for parkAttractions in res['parkAttractions']] if len(res['parkAttractions']) > 0 else 'Not available'}",
            'allies' : f"{[allies for allies in res['allies']] if len(res['allies']) > 0 else 'Not available'}",
            'enemies' : f"{[enemies for enemies in res['enemies']] if len(res['enemies']) > 0 else 'Not available'}",
            'name' : res['name'],
        }
        context = {
            'info': character
        }
        return render(request,'random_disney_character.html',context)

    else:
        return render(request,'error_page.html')

def reload_page(request):
  return redirect('/')