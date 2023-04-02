from django.db import models
from django.conf import settings


class Note(models.Model):
    title = models.CharField(max_length=100)
    comment = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)