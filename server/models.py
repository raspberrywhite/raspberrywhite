from django.db import models

class User(models.Model):
    id = models.SlugField(primary_key=True)
    username = models.CharField(max_length=200)
    email = models.CharField(max_length=200)