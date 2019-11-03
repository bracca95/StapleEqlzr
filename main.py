
from Player import *
from Filter import *
from scipy import signal

import array
from pydub import AudioSegment
from pydub.utils import get_array_type
from pydub.playback import play
from scipy.io.wavfile import write

if __name__=='__main__':
    path = 'media/american.mp3'
    
    player = Player(path)

    sound = AudioSegment.from_file(file=path)
    left = sound.split_to_mono()[0]

    bit_depth = left.sample_width * 8
    array_type = get_array_type(bit_depth)

    numeric_array = array.array(array_type, left._data)
    #print(numeric_array)

    # load song
    data = player.loadSong()

    # load filters
    filt1 = Filter()
    a = filt1.bandPass(64)

    # filter the song
    data2 = np.convolve(a, numeric_array)
    scaled = np.int16(data2/np.max(np.abs(data2)) * 32767)
    write('test.mp3', 44100, scaled)
    
    # play song (I could merge everything in one function but I do not always want to play)
    #player.playSong(data)