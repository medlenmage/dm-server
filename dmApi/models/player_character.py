from django.db import models
from django.conf import settings
from django.db.models.deletion import DO_NOTHING
from .campaigns import Campaign

class PlayerCharacter(models.Model):    
    character_sheet = models.URLField( max_length=250, unique=True, blank=True)