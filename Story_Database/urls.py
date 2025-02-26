from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('CharacterArticles/', views.CharacterArticles, name='CharacterArticles'),
    path('UniverseArticles/', views.UniverseArticles, name='UniverseArticles'),
    path('TalesAndChapters/', views.TalesAndChapters, name='TalesAndChapters'),
    path('Images/', views.Images, name='Images'),
    path('ProfilePage/', views.ProfilePage, name='ProfilePage'),
    
]