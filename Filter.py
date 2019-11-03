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

    # build a low-pass filter
    def lowPass(self, cut):
        return cut * np.sinc(cut * self.__n)

    # build a band-pass filter
    def bandPass(self, midcut):
        self.__bande.fillBands()
        if not self.__bande.getUpperList():
            print('empty band list!')
            return
        else:
            low, up = self.__bande.getLowerAndUpper(midcut)
            return up * np.sinc(up * self.__n) - low * np.sinc(low * self.__n)