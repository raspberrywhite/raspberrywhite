from django.db import models
from django.contrib.auth.models import User
from django.db.models import Q
import hotstuff
import time

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

    def can_play(self):
        now = int(round(time.time()))
        return (now - self.last_time_play) >= 3600


class RequestManager(models.Manager):
    def get_queryset(self):
        return super(RequestManager, self).get_queryset().order_by('priority')

    def get_max(self):
        return super(RequestManager, self).get_queryset().order_by('priority')[0]

class Request(models.Model):
    user = models.ForeignKey(Player)
    song = models.ForeignKey(Song)
    priority = models.BigIntegerField()
    now_play = models.BooleanField(default=False)
    requests = RequestManager()

    def save(self, *args, **kwargs):
        self.priority = self.user.last_time_req
        self.user.last_time_req = self.user.last_time_req + int(round(time.time()))
        if self.user.last_time_req >= 9223372036854775807:
            self.priority = 0
            self.user.last_time_req = 0
        self.user.save()
        super(Request, self).save(*args, **kwargs)
