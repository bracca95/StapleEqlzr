import numpy as np
import math
from Band import *

class Filter:

    # constructor
    def __init__(self):
        self.__w = np.linspace(-math.pi, math.pi, 1001)
        self.__M = 500
        self.__n = np.linspace(-(self.__M)/2, (self.__M)/2, self.__M)
        self.__bande = Band()
        self.__filtVal = []

    # build a low-pass filter
    def lowPass(self, cut):
        # frequencies must be normalized: cut/(Fs/2)
        self.__filtVal = cut/22100 * np.sinc(cut/22100 * self.__n)

    # build a band-pass filter
    def bandPass(self, midcut):
        self.__bande.fillBands()
        if not self.__bande.getUpperList():
            print('empty band list!')
            return
        else:
            low, up = self.__bande.getLowerAndUpper(midcut)
            self.__filtVal = up/22100 * np.sinc(up/22100 * self.__n) - low/22100 * np.sinc(low/22100 * self.__n)

    def getFilt(self):
        return self

    # return filter value
    def getFiltVal(self):
        return self.__filtVal