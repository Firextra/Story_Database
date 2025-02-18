from django.shortcuts import render
from .models import UniverseDatabase, CharacterDatabase

def home(request):
       universe=UniverseDatabase.objects.all()
       context={'universe':universe}
       return render(request, "index.html", context)
