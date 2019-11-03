
from Player import *
from Filter import *


if __name__=='__main__':
    path = 'media/american.mp3'
    
    player = Player(path)

    # load song
    data = player.loadSong()

    # load filters
    filt1 = Filter()
    filt1.bandPass(64)
    
    # play song (I could merge everything in one function but I do not always want to play)
    player.playSong(data)