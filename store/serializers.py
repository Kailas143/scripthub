from rest_framework import serializers
from .models import Script,Genre

class Category(object):
    def __init__(self,choices):
        self.choices=choices
SCRIPT_CATEGORY = (

    ('M', 'Movie'),
    ('S', 'Short Film'),
    ('D', 'Documentry'),
    ('T', 'Series')
)
MOVIE_CERTIFICATE = (
    ('U', 'U'), ('U/A', 'U/A'), ('A', 'A')
)



class ScriptSerializer(serializers.ModelSerializer):
    class Meta:
        model=Script
        fields='__all__'
        depth=1