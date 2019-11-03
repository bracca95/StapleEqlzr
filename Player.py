from pydub import AudioSegment
from pydub.playback import play
import io
import os

class Player:

    # parametrized constructor
    def __init__(self, songPath):
        self.__songPath = songPath

    ## methods ##
    # this returns raw data
    def loadSong(self):
        if self.__songPath == None:
            print('empty file or wrong path')
            return
        else:
            return open(self.__songPath, 'rb').read()

    # this plays the song
    def playSong(self, rawData):
        filename, file_extension = os.path.splitext(self.__songPath)
        song = AudioSegment.from_file(io.BytesIO(rawData), format=file_extension.strip('.'))
        play(song)