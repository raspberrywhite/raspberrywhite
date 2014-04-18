import player
from player import Mp3Player, PlayerListener
import time

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
        time.sleep(4)
        self.__player.play('tests/assets/test.mp3')

    def start(self):
        self.requestSong()

    def onStop(self):
        self.__player.shutdown()

if __name__ == '__main__':
    pop = Popmuzik()
    pop.start()