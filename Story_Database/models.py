from django.db import models

class UniverseDatabase(models.Model):
    Name=models.CharField(max_length=64)
    UniverseNumber=models.PositiveIntegerField(unique=True)
    UniverseDescription=models.TextField()

    def __str__(self):
        return (f" name:{self.Name}, universe number:{self.UniverseNumber}, universe description:{self.UniverseDescription}")



class CharacterDatabase(models.Model):
    Name = models.CharField(max_length=64)
    Author = models.CharField(max_length=64)
    CharacterDescription = models.TextField()
    UniverseNumber = models.PositiveIntegerField()

    def __str__(self):
        return (f" name:{self.Name}, author:{self.Author}, character description:{self.CharacterDescription}, universe number:{self.UniverseNumber}")