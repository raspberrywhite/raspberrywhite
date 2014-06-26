from django.contrib import admin

from server.models import Request
from server.models import Song

admin.site.register(Request)
admin.site.register(Song)