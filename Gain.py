import numpy as np

class Gain:

    # constructor
    def __init__(self):
        self.__gainVals = np.tile(0.0, 10)
        self.__min = -20
        self.__max = 20
        # self.__pop = [-1.6, 4,8, 7.2, 8, 5.6, 0, -2.1, -2.1, -1.6, -1.6]
        # self.__rock = [8, 4.8, -5.6, -8, -3.2, 4, 8.8, 11.2, 11.2, 11.2]

    # set gain for each preset and normalize it
    def setGain(self, num):
        if num == 0:
            __temp = [-1.6, 4.8, 7.2, 8, 5.6, 0, -2.1, -2.1, -1.6, -1.6] # self.__pop
        if num == 1:
            __temp = [8, 4.8, -5.6, -8, -3.2, 4, 8.8, 11.2, 11.2, 11.2]

        i=0
        while i < len(self.__gainVals):
            self.__gainVals[i] = __temp[i]
            self.__gainVals[i] = 2*((self.__gainVals[i] - self.__min)/(self.__max - self.__min)) -1
            i = i+1

    # normalization is neeeded!!
    def getGain(self, index):
        return self.__gainVals[index]