from django.db import models
from django.conf import settings
from django.db.models.deletion import DO_NOTHING
from .campaigns import Campaign
from .player_character import PlayerCharacter

class Player(models.Model):    
    campaigns = models.ForeignKey(Campaign, on_delete=models.DO_NOTHING, blank=True, null=True)
    player_characters = models.ForeignKey(PlayerCharacter, on_delete=models.DO_NOTHING, blank=True, null=True)