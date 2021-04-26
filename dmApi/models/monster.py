from django.db import models
from django.conf import settings
from django.db.models.deletion import DO_NOTHING

class Monster(models.Model):
    monster_title = models.TextField()
    monster_type = models.TextField()
    monster_stats = models.TextField()
    monster_skills = models.TextField()
    monster_notes = models.TextField()
