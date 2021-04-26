from django.db import models
from django.conf import settings
from django.db.models.deletion import DO_NOTHING

class NonPlayableCharacter(models.Model):
    npc_title = models.TextField()
    npc_type = models.TextField()
    npc_stats = models.TextField()
    npc_skills = models.TextField()
    npc_notes = models.TextField()