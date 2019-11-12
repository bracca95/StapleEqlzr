from pydub import AudioSegment
from pydub.playback import play
from pydub.utils import get_array_type
from scipy.io.wavfile import write
import array
import io
import os

class Player:

    # parametrized constructor
    def __init__(self, songPath):
        self.__songPath = songPath

    ## methods ##
    # https://stackoverflow.com/questions/9458480/read-mp3-in-python-3
    def loadSong(self):
        sound = AudioSegment.from_file(file=self.__songPath)    # out = AudioSegment
        left = sound.split_to_mono()[0]                         # in = AudioSegment, out = AudioSegment

        bit_depth = left.sample_width * 8                       # out = int. bith_depth=16 (try sound instead of left)
        array_type = get_array_type(bit_depth)                  # out = string. array_type=h
        numeric_array = array.array(array_type, left._data)     # out = array.array
        return numeric_array

    # this returns raw data
    def loadSong2(self):
        if self.__songPath == None:
            print('empty file or wrong path')
            return
        else:
            return open(self.__songPath, 'rb').read()

    # this plays the song
    def playSong2(self, rawData):
        filename, file_extension = os.path.splitext(self.__songPath)
        song = AudioSegment.from_file(io.BytesIO(rawData), format=file_extension.strip('.'))
        play(song)

p = Player('media/sample_song.mp3')
p.loadSong()
