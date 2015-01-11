from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.db.models import Q
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

    def play(self):
        now = int(round(time.time()))
        self.last_time_play = now
        self.save()

    def as_json(self):
        song_json = {}
        song_json['id'] = self.pk
        song_json['artist'] = self.artist
        song_json['title'] = self.title
        return song_json

class RequestManager(models.Manager):
    def get_queryset(self):
        return super(RequestManager, self).get_queryset().order_by('priority')

    def get_max(self):
        requests = super(RequestManager, self).get_queryset().order_by('priority')
        if len(requests) > 0:
            return requests[0]

    def next(self):
        try:
            now_request = super(RequestManager, self).get(now_play=True)
            now_request.delete()
        except:
            pass
        max_priority_request = self.get_max()
        if not max_priority_request:
            raise ObjectDoesNotExist()
        max_priority_request.now_play = True
        max_priority_request.save()
        return max_priority_request

class Request(models.Model):
    user = models.ForeignKey(Player)
    song = models.ForeignKey(Song)
    priority = models.BigIntegerField()
    now_play = models.BooleanField(default=False)
    requests = RequestManager()

    def save(self, *args, **kwargs):
        if not self.pk:
            self.priority = self.user.last_time_req
            self.user.last_time_req = self.user.last_time_req + int(round(time.time()))
            if self.user.last_time_req >= 9223372036854775807:
                self.priority = 0
                self.user.last_time_req = 0
            self.user.save()
        super(Request, self).save(*args, **kwargs)

    def as_json(self):
        request_json = {}
        request_json['artist'] = self.song.artist
        request_json['title'] = self.song.title
        request_json['now_play'] = self.now_play
        return request_json
