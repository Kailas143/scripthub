from django.contrib import admin
from .models import Script,Genre,MovieSearch
# Register your models here.


class GenreAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}
    search_fields=['name']

class ScriptAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('title',)}
    list_display=['title','director','writer','genredetail','year','rating']
    list_filter=['year','writer','language']
    ordering_by=['year',]
    search_fields=['genre']
    def genredetail(self,obj):
        return ','.join(c.name for c in obj.genre.all())
    

admin.site.register(Script,ScriptAdmin)
admin.site.register(Genre,GenreAdmin)
admin.site.register(MovieSearch)