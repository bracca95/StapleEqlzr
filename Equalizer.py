from Filter import *

class Equalizer:

    # constructor
    def __init__(self):
        self.__band = Filter().getMidBands()
        self.__filters = [Filter() for _ in range(len(self.__band))]

    # set filters parameters
    def setFilters(self):
        i = 0
        while i < len(self.__band):
            if i < 1:
                a = Filter()
                a.lowPass(32)
            else:
                a = Filter()
                a.bandPass(self.__band[i])
            
            self.__filters[i] = a.getFilt()
            i = i+1

    # get filter list
    def getFilters(self):
        return self.__filters