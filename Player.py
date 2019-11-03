from pydub import AudioSegment
from pydub.playback import play
import io

class Player:

    # parametrized constructor
    def __init__(self, path, formato):
        self.__path = path
        self.__formato = formato

    # methods
    def loadSong(self):
        return open(self.__path, 'rb').read()
    
    def playSong(self, rawData):
        song = AudioSegment.from_file(io.BytesIO(rawData), format=self.__formato)
        play(song)