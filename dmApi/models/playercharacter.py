from django.db import models
from django.conf import settings
from django.db.models.deletion import DO_NOTHING

class PlayerCharacter(models.Model):    
    character_sheet = models.TextField()