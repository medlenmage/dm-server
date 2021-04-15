from dmApi.models.dm import DungeonMaster
from django.db import models
from django.conf import settings
from django.db.models.deletion import DO_NOTHING
from .note import Note

class Campaign(models.Model):
    story = models.TextField()
    notes = models.ForeignKey(Note, on_delete=models.DO_NOTHING, blank=True, null=True)
    monsters = models.ForeignKey(Monster, on_delete=models.DO_NOTHING, blank=True, null=True)
    cheat_sheet = models.TextField()
    custom_rules = models.TextField()
    player_characters = models.ForeignKey(PlayerCharacter, on_delete=models.DO_NOTHING, blank=True, null=True)
    npc = models.ForeignKey(NPC, on_delete=models.DO_NOTHING, blank=True, null=True)
    dm = models.ForeignKey(DungeonMaster, on_delete=models.DO_NOTHING, blank=True, null=True)