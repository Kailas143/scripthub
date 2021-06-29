from django.shortcuts import get_object_or_404, render, redirect
from . models import Script, Genre, MovieSearch
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm,MovieSearchForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from rest_framework.response import Response
from .serializers import ScriptSerializer
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view, renderer_classes
from django.views.decorators.csrf import csrf_exempt


def home(request):
    recommended = Script.objects.filter(recommended=True)
    return render(request, 'store/home.html', {'recommended': recommended})


def all_scripts(request):
    scripts = Script.objects.all()
    return render(request, 'store/all_scripts.html', {'scripts': scripts})


def genre_items(request, genre_slug):
    genre = get_object_or_404(Genre, slug=genre_slug)
    scripts = Script.objects.filter(genre=genre)
    return render(request, 'store/genre_items.html', {'scripts': scripts})

@login_required(login_url='store:login_page')
def script_details(request, slug):
    scripts = Script.objects.get(slug=slug)
    script_genre = scripts.genre.first()
    similar_movies = Script.objects.filter(genre__name__endswith=script_genre)

    return render(request, 'store/script_details.html', {'scripts': scripts, 'similar_movies': similar_movies})


def register_page(request):
        if request.method=="POST":
                username=request.POST['name']
                email=request.POST['email']
                password=request.POST['password']
                password1=request.POST['password1']
                user=User.objects.create_user(username=username,email=email,password=password)
                user.save()
                return redirect('store:login_page')
        else:
                return render(request,'store/register.html')


def login_page(request):
        if request.method == "POST":
                username = request.POST.get('username')
                password = request.POST.get('password')
                user = authenticate(request, username=username, password=password)
                if user is not None:
                        login(request, user)
                        return redirect('store:home')
                else:
                        messages.info(request, 'Invalid Details')
        return render(request,'store/login.html',{})


def signout(request):
    context = {}
    logout(request)
    context['error'] = "You have been logged out"
    return render(request, 'store/login.html', context)

def search_box(request):
        searched_movies = Script.objects.filter(title__icontains = request.POST.get('name_of_movie',None))
        return render(request, 'search_book.html', {'searched_movies':searched_movies})


@api_view(('GET',))
@csrf_exempt
def script_list(request):
        if request.method=="GET":
                scripts=Script.objects.all()
                serializer=ScriptSerializer(scripts,many=True)
                return Response(serializer.data)
        elif request.method=="POST":
               data=JSONParser().parser(request)
               serializer=ScriptSerializer(data=data)
               if serializer.is_valid():
                       serializer.save()
                       return Response(serializer.data)
               return Response(serializer.errors,status=400)




