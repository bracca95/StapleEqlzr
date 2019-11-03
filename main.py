
from Player import *


if __name__=='__main__':
    path = 'media/american.mp3'
    formato = 'mp3'

    player = Player(path, formato)

    # play song
    data = player.loadSong()
    player.playSong(data)