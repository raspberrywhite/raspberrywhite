from django.db import models
from django.contrib.auth.models import User
from django.db.models import Q

class Player(models.Model):
    user = models.OneToOneField('auth.User', primary_key=True, related_name='player')
    last_time_req = models.BigIntegerField(default=0)


class SongManager(models.Manager):
    def query(self, q):
        return super(SongManager, self).get_queryset().filter(Q(title__icontains = q)|Q(artist__icontains = q ))

class Song(models.Model):
    title = models.TextField()
    artist = models.TextField()
    path = models.TextField(blank=True)
    last_time_play = models.BigIntegerField(default=0)
    songs = SongManager()

class Request(models.Model):
    user = models.ForeignKey(Player)
    song = models.ForeignKey(Song)
    priority = models.BigIntegerField()
    now_play = models.BooleanField(default=False)