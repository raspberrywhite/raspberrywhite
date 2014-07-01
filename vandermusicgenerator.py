import os
import eyed3

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "servant.settings")

from server import models

# From now onwards start your script..

mypath = 'songs/'

for f in os.listdir(mypath):
    path = os.path.join(mypath,f)
    af = eyed3.load(path)
    artist = af.tag.artist
    title = af.tag.title
    song = models.Song()
    song.path = path
    song.title = title
    song.artist = artist
    song.save()