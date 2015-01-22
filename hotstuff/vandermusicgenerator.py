import os
import eyed3
from server import models

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "servant.settings")

def generate(songs_path):
    for f in os.listdir(songs_path):
        path = os.path.join(songs_path,f)
        af = eyed3.load(path)
        if not af:
            continue
        artist = af.tag.artist
        title = af.tag.title
        if models.Song.songs.filter(title = title, artist = artist).exists():
            continue
        song = models.Song()
        song.path = path
        song.title = title
        song.artist = artist
        song.save()