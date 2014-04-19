import player
from player import Mp3Player, PlayerListener
import time
import requests

class Popmuzik():

    class Mp3Listener(PlayerListener):
        def __init__(self, popmuzik):
            self.__popmuzik = popmuzik
        def onStop(self):
            self.__popmuzik.onStop()
            self.__popmuzik.requestSong()

    def __init__(self):
        self.__player = player.Mp3Player()
        self.__listener = Popmuzik.Mp3Listener(self)
        self.__player.attachListener(self.__listener)

    def requestSong(self):
        r = requests.get('http://localhost:8000/songs/next')
        if r.status_code == 200:
            song_json = r.json()
            if 'path' in song_json:
                self.__player.play(song_json['path'])
        elif r.status_code == 404:
            time.sleep(10)
            self.requestSong()

    def start(self):
        self.requestSong()

    def onStop(self):
        self.__player.shutdown()

if __name__ == '__main__':
    pop = Popmuzik()
    pop.start()