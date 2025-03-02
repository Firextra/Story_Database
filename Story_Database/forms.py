from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import CharacterDatabase, UniverseDatabase, ChaptersDatabase, TalesDatabase

class RegisterForm(UserCreationForm):   #RegisterForm an extension of UserCreationForm
    email = forms.EmailField()      #add email to register form

    class Meta:
        model = User        #model takes djangos User model
        fields = ["username", "email", "password1", "password2"]    #fields that the user can enter

class CharacterForm(forms.ModelForm):
    class Meta:
        model = CharacterDatabase   #model takes Character Database model
        fields = ["Name", "CharacterDescription", "UniverseNumber", "Tags"] #fields that can be entered or selected (UniverseNumber is foreign and must be selected from Universe Database
                                                                            #and Tags shows any relation to other characters and so is a dropdown bar showing characters from Character Database)

class UpdateCharacterForm(CharacterForm): #UpdateCharacterForm an extension of CharacterForm
    class Meta:
        model = CharacterDatabase
        fields = ["Name", "CharacterDescription", "UniverseNumber", "Tags"]

class UniverseForm(forms.ModelForm):    
    class Meta:
        model = UniverseDatabase   #model takes Universe Database model
        fields = ["Name", "UniverseDescription", "UniverseNumber"] 

class UpdateUniverseForm(UniverseForm): #UpdateUniverseForm an extension of UniverseForm
    class Meta:
        model = UniverseDatabase   #model takes Universe Database model
        fields = ["Name", "UniverseDescription", "UniverseNumber"] 

class ChapterForm(forms.ModelForm):
    class Meta:
        model = ChaptersDatabase   #model takes Chapter Database model
        fields = ["Name", "Chapter", "UniverseNumber"] 

class UpdateChapterForm(ChapterForm):  #UpdateChapterForm an extension of ChapterForm
    class Meta:
        model = ChaptersDatabase   #model takes Chapter Database model
        fields = ["Name", "Chapter", "UniverseNumber"] 

class TaleForm(forms.ModelForm):
    class Meta:
        model = TalesDatabase   #model takes Tales Database model
        fields = ["Name", "Tale", "Character"] 

class UpdateTaleForm(TaleForm):  #UpdateTaleForm an extension of TaleForm
    class Meta:
        model = TalesDatabase   #model takes Tales Database model
        fields = ["Name", "Tale", "Character"] 