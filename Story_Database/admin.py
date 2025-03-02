from django.contrib import admin
from . models import UniverseDatabase, CharacterDatabase, Profile, TalesDatabase, ChaptersDatabase

admin.site.register(UniverseDatabase) #putting the models (databases) into the admin page
admin.site.register(CharacterDatabase)
admin.site.register(Profile)
admin.site.register(ChaptersDatabase)
admin.site.register(TalesDatabase)