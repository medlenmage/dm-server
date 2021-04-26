from django.db import models
from django.conf import settings
from django.db.models.deletion import DO_NOTHING

class Note(models.Model):
    note_title = models.TextField()
    note_body = models.TextField()
    note_date = models.DateField()
