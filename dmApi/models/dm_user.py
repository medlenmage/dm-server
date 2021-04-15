from dmApi.models.dm import DungeonMaster
from django.db import models
from django.conf import settings
from django.db.models.deletion import DO_NOTHING
from .campaigns import Campaign

class DMUser(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    bio = models.TextField()
    phone_number = models.TextField()
    dungeon_master = models.ForeignKey(DungeonMaster, on_delete=models.DO_NOTHING, blank=True, null=True)
    player = dungeon_master = models.ForeignKey(Player, on_delete=models.DO_NOTHING, blank=True, null=True)