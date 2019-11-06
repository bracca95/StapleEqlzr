import numpy as np

class Preset:

    def __init__(self):
        # 10 band equalizer
        self.__val = np.tile(0.0, 10)

    # read a txt file where presets are stored
    def readPreset(self, num):
        with open('utilities/presets.txt', 'r') as fp:
            line = fp.readline()
            i = 1
            while line:
                line = line.strip('qwertyuiopasdfghjklzxcvbnm:')
                arr = line.split('   ')
                
                idx = 0
                while idx < len(arr):
                    self.__val[idx] = (float(arr[idx]))
                    idx += 1
                
                if num==i:
                    # print(val)
                    self.__val = self.__val
                    return
                else:
                    line = fp.readline()
                    i += 1
                    
    def getPreset(self):
        return self.__val
