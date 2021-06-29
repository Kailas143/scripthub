from . models import Script,Genre

def genre_list(request):
    genres=Genre.objects.all()
    return{
        'genres':genres
    }