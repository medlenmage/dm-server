from django.db import models
from django.conf import settings
from django.db.models.deletion import DO_NOTHING

class Campaign(models.Model):
    story = models.TextField()
    notes = models.ForeignKey(Note, on_delete=models.DO_NOTHING, blank=True, null=True)
    monsters = models.ForeignKey(Monster, on_delete=models.DO_NOTHING, blank=True, null=True)
    cheat_sheet = models.TextField()
    custom_rules = models.TextField()