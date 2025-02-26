from django.shortcuts import render, redirect
from .models import UniverseDatabase, CharacterDatabase
from .forms import RegisterForm


def index(request):
       universe=UniverseDatabase.objects.all()
       context={'universe':universe}
       return render(request, "index.html", context)

def CharacterArticles(request):
       return render(request, "CharacterArticles.html")

def UniverseArticles(request):
       return render(request, "UniverseArticles.html")

def TalesAndChapters(request):
       return render(request, "TalesAndChapters.html")

def Images(request):
       return render(request, "Images.html")

def ProfilePage(request):
       return render(request, "ProfilePage.html")

def register(response):
       if response.method == "POST":
              form = RegisterForm(response.POST)
              if form.is_valid():
                     form.save()
                     return redirect("/")
       else:
              form = RegisterForm()

       return render(response, "register.html", {"form":form})



