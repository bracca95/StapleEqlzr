
from Player import *
from Equalizer import *
from Gain import Gain
from scipy import signal

if __name__=='__main__':

    # load song as numeric array
    path = 'media/american.mp3'
    player = Player(path)
    numeric_array = player.loadSong()

    eq = Equalizer()
    eq.setFilters()
    filterList = eq.getFilters()

    g = Gain()
    g.setGain(1)

    data = 0
    i = 0
    while i < len(filterList):
        data = data + np.multiply(g.getGain(i), np.convolve(filterList[i].getFiltVal(), numeric_array))
        i = i+1
    
    # save song
    # https://stackoverflow.com/questions/10357992/how-to-generate-audio-from-a-numpy-array
    scaled = np.int16(data/np.max(np.abs(data)) * 32767)
    write('test.mp3', 44100, scaled)
    
    # play song (I could merge everything in one function but I do not always want to play)
    # player.playSong(data2)