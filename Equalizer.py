from Filter import *

class Equalizer:

    def __init__(self):
        self.__band = [32, 64, 125, 250, 500, 1000, 2000, 4000, 8000, 16000]
        self.__filters = [Filter() for _ in range(len(self.__band))]

    def setFilters(self):
        i = 0
        while i < len(self.__band):
            if i < 1:
                a = Filter()
                a.lowPass(32)
                self.__filters[i] = a.getFilt()
            else:
                a = Filter()
                a.bandPass(self.__band[i])
                self.__filters[i] = a.getFilt()
            i = i+1

    def getFilters(self):
        return self.__filters
