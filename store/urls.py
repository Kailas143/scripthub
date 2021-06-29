from django.urls import path
from .import views

app_name='store'

urlpatterns = [
    path('', views.all_scripts,name='all_scripts'),
    path('home',views.home,name='home'),
    path('<slug:genre_slug>',views.genre_items,name='genre_items'),
    path('script/<slug:slug>',views.script_details,name='script_details'),
    path('register/',views.register_page,name='register_page'),
    path('search/',views.search_box,name='search_box'),
    path('login/',views.login_page,name='login_page'),
    path('logout/',views.signout,name='signout'),
    path('scripts/',views.script_list,name='script_list'),
    
]
