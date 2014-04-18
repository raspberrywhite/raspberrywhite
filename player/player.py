class Player():

    PAUSE = 2
    PLAY = 1
    STOP = 0

    def __init__(self):
        self.listeners = []
        self.__status = 0

    def attachListener(self, listener):
        self.listeners.append(listener)

    def getStatus(self):
        return self.__status

    def isPlaying(self):
        return self.__status == Player.PLAY

    def play(self, source):
        self.__status = Player.PLAY
        for listener in self.listeners:
            listener.onPlay(source)

    def stop(self):
        self.__status = Player.STOP
        for listener in self.listeners:
            listener.onStop()

    def pause(self):
        self.__status = Player.PAUSE
        for listener in self.listeners:
            listener.onPause()

    def resume(self):
        self.__status = Player.PLAY
        for listener in self.listeners:
            listener.onResume()

    def shutdown(self):
        self.__status = Player.STOP
        for listener in self.listeners:
            listener.onShutdown()

    def _content_parser(self):
        pass