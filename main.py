
from Player import *

path = 'media/american.mp3'
formato = 'mp3'

player = Player(path, formato)
song = player.loadSong()
player.playSong()