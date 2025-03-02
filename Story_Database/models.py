from django.db import models
from django.contrib.auth.models import User


class UniverseDatabase(models.Model):   #Universe Database
    Name=models.CharField(max_length=64)
    UniverseAuthor=models.CharField(max_length=64, null=True)   #can be left empty, since multiple authors for a Universe could exist since they can be large projects of work
    UniverseNumber=models.PositiveIntegerField(unique=True)     #primary key using unique=True
    UniverseDescription=models.TextField() #textfield for the description that can vary in size depending on how creative the user is

    def __str__(self):
        return (f" name:{self.Name}, universe number:{self.UniverseNumber}, universe description:{self.UniverseDescription}")



class CharacterDatabase(models.Model):  #Character database
    Name = models.CharField(max_length=64)
    Author = models.CharField(max_length=64, editable=False)   #the author is not editable, it is linked to the account that made it
    CharacterDescription = models.TextField()
    UniverseNumber = models.ForeignKey(UniverseDatabase, on_delete=models.CASCADE)  #foreign key to Unieverse Database, and so upon deletion of a universe no characters from it exist and so .cascade is added
    Tags = models.ManyToManyField("self", blank=True, symmetrical=False)    #relations to other characters from Character database  (symmetrical since it doesnt go both ways always) blank because it can be left empty

    def __str__(self):
        return (f" name:{self.Name}, author:{self.Author}, character description:{self.CharacterDescription}, universe number:{self.UniverseNumber}")
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)     #deletes Profile if User account is deleted
    image = models.ImageField(default='default1.jpg', upload_to='profile_pics', null=True, blank=True) #profile picture, with defaults in place, can be left empty (default should deal with it being empty)
    role = models.CharField(default='Visionary', max_length=64, null=True, blank=True) #roles only assignable by staff, any user is a visionary on first login and could change with time

    def __str__(self):
        return (f" user:{self.user}, image:{self.image}, role:{self.role}")
    
class TalesDatabase(models.Model):
    Name = models.CharField(max_length=64)
    Author = models.CharField(max_length=64, editable=False)    #cant be editted
    Tale = models.TextField()
    Character = models.ForeignKey(CharacterDatabase, blank=False, on_delete=models.CASCADE) #foreign key, deletes using CASCADE

    def __str__(self):
        return(f" name:{self.Name}, Author:{self.Author}, Tale:{self.Tale}, Character:{self.Character}")

class ChaptersDatabase(models.Model):
    Name = models.CharField(max_length=64)
    Author = models.CharField(max_length=64, editable=False) #cant be editted
    Chapter = models.TextField()
    UniverseNumber = models.ForeignKey(UniverseDatabase, on_delete=models.CASCADE) #foreign game