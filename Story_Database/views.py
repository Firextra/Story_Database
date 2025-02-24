from django.shortcuts import render
from .models import UniverseDatabase, CharacterDatabase
from django.contrib.auth.decorators import login_required


def home(request):
       universe=UniverseDatabase.objects.all()
       context={'universe':universe}
       return render(request, "index.html", context)

@login_required
def Profile(request):
       return render(request, 'ProfilePage.html')