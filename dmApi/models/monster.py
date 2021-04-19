from django.db import models
from django.conf import settings
from django.db.models.deletion import DO_NOTHING

class Monster(models.Model):
    monster_title = models.TextField()
    monster_type = models.TextField()
    monster_stats = models.DateTimeField()
    monster_skills = models.DateTimeField()
    monster_notes = models.DateTimeField()
