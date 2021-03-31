from django.db import models
from django.conf import settings
from django.db.models.deletion import DO_NOTHING

class DungeonMaster(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    bio = models.TextField()
    phone_number = models.TextField()
    campaigns = models.ForeignKey(Campaign, on_delete=models.DO_NOTHING, blank=True, null=True)
    