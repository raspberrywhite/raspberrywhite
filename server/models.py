from django.db import models
from django.contrib.auth.models import User

class Player(models.Model):
    user = models.OneToOneField('auth.User', primary_key=True, related_name='player')
    last_time_req = models.BigIntegerField(default=0)

class Song(models.Model):
    title = models.TextField()
    artist = models.TextField()
    path = models.TextField(blank=True)
    last_time_play = models.BigIntegerField(default=0)

class Request(models.Model):
    user = models.ForeignKey(Player)
    song = models.ForeignKey(Song)
    priority = models.BigIntegerField()
    now_play = models.BooleanField(default=False)