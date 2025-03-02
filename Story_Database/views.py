from django.shortcuts import render, redirect, get_object_or_404
from .models import UniverseDatabase, CharacterDatabase, TalesDatabase, ChaptersDatabase
from .forms import RegisterForm, CharacterForm, UpdateCharacterForm, UniverseForm, UpdateUniverseForm, TaleForm, UpdateTaleForm, ChapterForm, UpdateChapterForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required 
import random

#request to view
def index(request):
       CharacterDataBase=CharacterDatabase.objects.all()       #create instance 
       TaleDatabase=TalesDatabase.objects.all()
       ChapterDatabase=ChaptersDatabase.objects.all()
       Character = random.choice(CharacterDataBase)
       Tale = random.choice(TaleDatabase)
       Chapter = random.choice(ChapterDatabase)
       context={'Character':Character, 'Tale':Tale, 'Chapter':Chapter}
       return render(request, "index.html", context)

def CharacterArticles(request): #basic request for http and so a html file is given
       return render(request, "CharacterArticles.html")

def UniverseArticles(request):
       return render(request, "UniverseArticles.html")

def TalesAndChapters(request):
       return render(request, "TalesAndChapters.html")

def ProfilePage(request):
       return render(request, "ProfilePage.html")

def ModPage(request):
       return render(request)

def register(response):     #registering an account using Django
       if response.method == "POST": #ensures that the user has been sent by POST (via link) and not GOT (via URL)
              form = RegisterForm(response.POST) #create form instance of register form with the data from POST
              if form.is_valid():  #check that the form (registering of account) is valid
                     form.save()   #saves if the account is valid
                     return redirect("/login/") #redirects to the login screen after successfully creating an account so they can login
       else:         
              form = RegisterForm() #create empty form

       return render(response, "register.html", {"form":form})  #return back to the register and form to django and find issues for registering account

@login_required       #logged in only
def DeleteAccountConfirm(request):
       if request.method == "POST":       #ensures its POST and not GET
              return render(request, "DeleteAccountConfirm.html")
       return redirect("/ProfilePage")  #redirect users back to their profile page if they got to account delete via GOT (Could have issues if not logged in and type /DeleteAccountConfirm)

@login_required      #logged in only
def DeleteAccount(request):
       if request.method =="POST": #ensures its POST and not GET
              user = request.user  #get user
              logout(request)      #sends a logout for current user
              user.delete()        #delete user
              return redirect("/") #take back to the home screen
       return redirect("/ProfilePage") #redirect those who used GOT to get to account deletion (Could have issues if not logged in and type /DeleteAccountConfirm)

def CharacterArticles(request):
       Universes=UniverseDatabase.objects.order_by("UniverseNumber") #create Universes which is the model of UniverseDatabase but orders it based on Universe Number
       CharacterDictionary = {     #create a dictionary storing characters with their relevant universe they live in (foreign key)
              universe: CharacterDatabase.objects.filter(UniverseNumber=universe).order_by("Name") #ordered by name so characters can be found in their universe alphabetically
              for universe in Universes #loops for each universe for all Universes (Database)
       }

       for universe, characters in CharacterDictionary.items():
        print(f"Universe: {universe.Name}, Characters: {characters.count()}")

       context = {"CharacterDictionary":CharacterDictionary} #create context for teh dictionary for html file
       return render(request, "CharacterArticles.html", context) #render the html file and send the context

def CharacterPage(request, CharacterID): #take in CharacterID
       Character=get_object_or_404(CharacterDatabase, id=CharacterID) #get_object_or_404 attempts to retrieve object if fails show http 404 error, the character looked for is in CharacterID
       User = request.user.username #fetch username of person to check if individual is author in the html
       context = {"Character":Character, "User":User} #create context for character for html
       return render(request, "CharacterPage.html", context) 

def CreateCharacter(request):
       if request.method == "POST": #Ensure that only those who got here used POST and not GOT since the button checks if the user is logged in and if bypassed via typing in url, this stops that
              form = CharacterForm(request.POST) #gets form characterForm from form.py and data with it
              if form.is_valid():  #checks form is valid
                     character = form.save(commit=False) #dont save the data yet to the database as author needs to be assigned
                     character.Author = request.user.username #request teh users username and put that in the author
                     character.save() #save the form to database
                     return redirect("/CharacterArticles")  #redirects the user to the page of character articles to see their work
       else:
              form = CharacterForm() #empty form
       
       return render(request, "CreateCharacter.html",  {"form":form}) #attempt to do it again as error occured

def CharacterUpdate(request, CharacterID):
       Character = Character=get_object_or_404(CharacterDatabase, id=CharacterID)  #fetch the character
       if request.method == "POST":
              form = UpdateCharacterForm(request.POST, instance=Character)
              if form.is_valid():  #checks form valid
                     form.save()    #saves form
                     return redirect("/CharacterArticles")
       else:
              form = UpdateCharacterForm(instance=Character)   #resets form for retry
       
       return render(request, "CharacterUpdate.html", {"form":form})
       

def UniverseArticles(request):
       Universes=UniverseDatabase.objects.order_by("UniverseNumber") #create Universes which is the model of UniverseDatabase but orders it based on Universe Number
       context = {"Universes":Universes} #create context for teh dictionary for html file
       return render(request, "UniverseArticles.html", context) #render the html file and send the context

def UniversePage(request, UniverseNumber): #take in CharacterID
       Universe=get_object_or_404(UniverseDatabase, universe=Universe.id) #get_object_or_404 attempts to retrieve object if fails show http 404 error, the character looked for is in CharacterID
       User = request.user.username #fetch username of person to check if individual is author in the html
       context = {"Universe":Universe, "User":User} #create context for character for html
       return render(request, "UniversePage.html", context) 

def CreateUniverse(request):
       if request.method == "POST": #Ensure that only those who got here used POST and not GOT since the button checks if the user is logged in and if bypassed via typing in url, this stops that
              form = UniverseForm(request.POST) #gets form characterForm from form.py and data with it
              if form.is_valid():  #checks form is valid
                     Universe = form.save(commit=False) #dont save the data yet to the database as author needs to be assigned
                     Universe.Author = request.user.username #request teh users username and put that in the author
                     Universe.save() #save the form to database
                     return redirect("/UniverseArticles/")  #redirects the user to the page of character articles to see their work
       else:
              form = UniverseForm() #empty form
       
       return render(request, "CreateUniverse.html",  {"form":form}) #attempt to do it again as error occured

def UniverseUpdate(request, UniverseNumber):
       Universe = Universe=get_object_or_404(UniverseDatabase, UniverseNumber=UniverseNumber)  #find record that needs updating with the UniverseNumber
       if request.method == "POST":
              form = UpdateUniverseForm(request.POST, instance=Universe) #create a form and inserts the data from the record into the form using instance=
              if form.is_valid():
                     form.save()
                     return redirect("/UniverseArticles/")
       else:
              form = UpdateUniverseForm(instance=Universe) #retry form with the records data in the fields 
       
       return render(request, "UniverseUpdate.html", {"form":form})

def TalesAndChapters(request):
       Universes=UniverseDatabase.objects.order_by("UniverseNumber") #create Universes which is the model of UniverseDatabase but orders it based on Universe Number
       Characters =CharacterDatabase.objects.order_by("Name")
       TaleDictionary = { #create dictionary of characters and associated tales
              character: TalesDatabase.objects.filter(Character=character).order_by("Name")  #sorted alphabetically
              for character in Characters #repeat for each character in the character database
       }

       ChapterDictionary = {  #create a dicitonary with Universes and the chapters associated with each one
              universe: ChaptersDatabase.objects.filter(UniverseNumber=universe).order_by("Name") #sorted by name
              for universe in Universes #repeat for each universe in the universe database
       }

       context = {"TaleDictionary":TaleDictionary, "ChapterDictionary":ChapterDictionary} #create context for the dictionary for html file

       return render(request, "TalesAndChapters.html", context) #render the html file and send the context

def TalePage(request, TaleID): #take in TaleID
       Tale=get_object_or_404(TalesDatabase, id=TaleID) #get_object_or_404 attempts to retrieve object if fails show http 404 error, the character looked for is in TaleID
       User = request.user.username #fetch username of person to check if individual is author in the html
       context = {"Tale":Tale, "User":User} #create context for character for html
       return render(request, "TalePage.html", context) 

def CreateTale(request):
       if request.method == "POST": #Ensure that only those who got here used POST and not GOT since the button checks if the user is logged in and if bypassed via typing in url, this stops that
              form = TaleForm(request.POST) #gets form TaleForm from form.py and data with it
              if form.is_valid():  #checks form is valid
                     Tale = form.save(commit=False) #dont save the data yet to the database as author needs to be assigned
                     Tale.Author = request.user.username #request the users username and put that in the author
                     Tale.save() #save the form to database
                     return redirect("/TalesAndChapters/")  #redirects the user to the page of character articles to see their work
       else:
              form = TaleForm() #empty form
       
       return render(request, "CreateTale.html",  {"form":form}) #attempt to do it again as error occured

def TaleUpdate(request, TaleID):
       Tale = Tale=get_object_or_404(TalesDatabase, id=TaleID) #get the record needing update
       if request.method == "POST":
              form = UpdateTaleForm(request.POST, instance=Tale) #insert the information onto the form
              if form.is_valid():#form validation
                     form.save() #save
                     return redirect("/TalesAndChapters/")
       else:
              form = UpdateTaleForm(instance=Tale) #redo form
       
       return render(request, "TaleUpdate.html", {"form":form})

def ChapterPage(request, ChapterID): #take in ChapterID
       Chapter=get_object_or_404(ChaptersDatabase, id=ChapterID) #get_object_or_404 attempts to retrieve object if fails show http 404 error, the character looked for is in ChapterID
       User = request.user.username #fetch username of person to check if individual is author in the html
       context = {"Chapter":Chapter, "User":User} #create context for character for html
       return render(request, "ChapterPage.html", context) 

def CreateChapter(request):
       if request.method == "POST": #Ensure that only those who got here used POST and not GOT since the button checks if the user is logged in and if bypassed via typing in url, this stops that
              form = ChapterForm(request.POST) #gets form ChapterForm from form.py and data with it
              if form.is_valid():  #checks form is valid
                     Chapter = form.save(commit=False) #dont save the data yet to the database as author needs to be assigned
                     Chapter.Author = request.user.username #request the users username and put that in the author
                     Chapter.save() #save the form to database
                     return redirect("/TalesAndChapters/")  #redirects the user to the page of character articles to see their work
       else:
              form = ChapterForm() #empty form
       
       return render(request, "CreateChapter.html",  {"form":form}) #attempt to do it again as error occured

def ChapterUpdate(request, ChapterID):
       Chapter = Chapter=get_object_or_404(ChaptersDatabase, id=ChapterID) #get the record using ChapterID from database
       if request.method == "POST":
              form = UpdateChapterForm(request.POST, instance=Chapter) #create form for html that has the data on the record on the form
              if form.is_valid(): #validation
                     form.save() #save
                     return redirect("/TalesAndChapters/")
       else:
              form = UpdateChapterForm(instance=Chapter) #redo form
       
       return render(request, "ChapterUpdate.html", {"form":form})
