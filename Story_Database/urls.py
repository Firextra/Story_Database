from django.urls import path
from . import views

urlpatterns = [ #links to the pages
    path('', views.index, name='index'),
    path('CharacterArticles/', views.CharacterArticles, name='CharacterArticles'),
    path('UniverseArticles/', views.UniverseArticles, name='UniverseArticles'),
    path('TalesAndChapters/', views.TalesAndChapters, name='TalesAndChapters'),
    path('ProfilePage/', views.ProfilePage, name='ProfilePage'),
    path('admin/', views.ModPage, name="ModPage"),
    path('DeleteAccount/', views.DeleteAccount, name="DeleteAccount"),
    path('DeleteAccount/Confirm/', views.DeleteAccountConfirm, name="DeleteAccountConfirm"),
    path('CharacterPage/<int:CharacterID>/', views.CharacterPage, name="CharacterPage"), #<int:CharacterID> has the ID for the page
    path('CharacterArticles/Create/', views.CreateCharacter, name="CreateCharacter"),
    path('CharacterArticles/<int:CharacterID>/Update/', views.CharacterUpdate, name="CharacterUpdate"),
    path('UniversePage/<int:UniverseNumber>/', views.UniversePage, name="UniversePage"),
    path('UniverseArticles/Create/', views.CreateUniverse, name="CreateUniverse"),
    path('UniverseArticles/<int:UniverseNumber>/Update/', views.UniverseUpdate, name="UniverseUpdate"),
    path('TalesAndChapters/', views.TalesAndChapters, name="TalesAndChapters"),
    path('TalePage/<int:TaleID>/', views.TalePage, name="TalePage"), #<int:TaleID> has the ID for the page
    path('TalesAndChapters/CreateTale/', views.CreateTale, name="CreateTale"),
    path('Tales/<int:TaleID>/Update/', views.TaleUpdate, name="TaleUpdate"),
    path('ChapterPage/<int:ChapterID>/', views.ChapterPage, name="ChapterPage"), #<int:ChapterID> has the ID for the page
    path('TalesAndChapters/CreateChapter/', views.CreateChapter, name="CreateChapter"),
    path('Chapters/<int:ChapterID>/Update/', views.ChapterUpdate, name="ChapterUpdate"),
    path('register/', views.register, name='register')
]