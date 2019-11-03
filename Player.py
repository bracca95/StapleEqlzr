from pydub import AudioSegment
from pydub.playback import play
import io

class Player:
    # private variables
    __rawData = None
    __song = None
    __path = None
    __formato = None

    # parametrized constructor
    def __init__(self, path, formato):
        self.__rawData = None
        self.__song = None
        self.__path = path
        self.__formato = formato

    # methods
    def loadSong(self):
        self.__rawData = open(self.__path, 'rb').read()
    
    def playSong(self):
        self.__song = AudioSegment.from_file(io.BytesIO(self.__rawData), format=self.__formato)
        play(self.__song)