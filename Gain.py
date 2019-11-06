import numpy as np
from Preset import Preset

class Gain:

    # constructor
    def __init__(self):
        self.__gainVals = np.tile(0.0, 10)
        self.__min = -20
        self.__max = 20
        self.__preset = Preset()

    # set gain for each preset and normalize it
    def setGain(self, num):
        self.__preset.readPreset(num)
        self.__gainVals = self.__preset.getPreset()

        i=0
        while i < len(self.__gainVals):
            # normalization
            self.__gainVals[i] = 2*((self.__gainVals[i] - self.__min)/(self.__max - self.__min)) -1
            i = i+1

    # normalization is neeeded!!
    def getGain(self, index):
        return self.__gainVals[index]