from django.db import models

class User(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True)
    username = models.TextField(blank=True)
    email = models.TextField(blank=True)
    is_admin = models.BooleanField(default=False)
    last_request = models.BigIntegerField()

class Song(models.Model):
    id = models.BigIntegerField(primary_key=True)
    title = models.TextField(blank=True)
    artist = models.TextField(blank=True)
    path = models.TextField(blank=True)

class Request(models.Model):
    user = models.ForeignKey(User)
    song = models.ForeignKey(Song)
    priority = models.BigIntegerField()