from django.db import models
from django.contrib.auth.models import User

class Player(models.Model):
    user = models.OneToOneField('auth.User', primary_key=True, related_name='player')
    last_time_req = models.BigIntegerField(default=0)

class Song(models.Model):
    id = models.BigIntegerField(primary_key=True)
    title = models.TextField(blank=True)
    artist = models.TextField(blank=True)
    path = models.TextField(blank=True)

class Request(models.Model):
    user = models.ForeignKey(Player)
    song = models.ForeignKey(Song)
    priority = models.BigIntegerField()