
class Band:

    # constructor
    def __init__(self):
        self.__band = [32, 64, 125, 250, 500, 1000, 2000, 4000, 8000, 16000]
        self.__lower = [33]
        self.__upper = []

    # a band-pass filter is made up of an lower cut and an upper cut frequencies. 
    # given the previous' upper bound, which is the lower of the current, retrieve the next upper
    def fillBands(self):
        i = 0

        # read all the cut frequencies
        while i < len(self.__band) - 1 :
            # get the upperbound
            up = 2 * self.__band[i+1] - self.__lower[i]
            self.__upper.append(up)
            
            # get the next lower bound by summing 1 to the found upperbound
            if self.__upper[i] < 20000:
                self.__lower.append(up+1) # exclude last
            
            # update index
            i = i+1

    def getUpperList(self):
        return self.__upper

    def getLowerList(self):
        return self.__lower

    # given a mid cut frequency, return its lower and upper bound
    def getLowerAndUpper(self, val):
        i = 0
        
        while i < len(self.__band) - 1 :
            if val != self.__band[i]:
                i = i+1
            else:
                return self.__lower[i-1], self.__upper[i-1]
                
        print('unknown value. choose between [64, 125, 250, 500, 1000, 2000, 4000, 8000, 16000]')
        return




# debug
# ciao = Band()
# ciao.upperList()

# print(ciao.lower)
# print(ciao.upper)