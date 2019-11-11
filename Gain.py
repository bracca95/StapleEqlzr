import numpy as np
from utilities.preset_json_reader import *
import json

class Gain:

    # constructor
    def __init__(self):
        self.__gainVals = np.tile(0.0, 10)
        self.__min = -15
        self.__max = 15
        self.__preset = None

    # load json data and return a string
    def loadGain(self):
        with open('utilities/presets.json') as json_file:
	        data = json.load(json_file)							            # in = .json, out = dict
	        json_string = json.dumps(data)						            # in = dict, out = string
	        self.__preset = preset_from_dict(json.loads(json_string))	# in = string, out = Preset
    
    # set gain for each preset and __normalize it__
    def setGain(self, index):
        i = 0
        # get all the configurations (presets)
        while i < len(self.__preset.configurations):
            # if preset id == user choice
            if self.__preset.configurations[i].id == index:
                # read the data (only one list for preset)
                temp = self.__preset.configurations[i].data[0]
                # temp is a dict, so retrieve values from keys
                j = 0
                for key, value in temp.items():
                    # normalization
                    self.__gainVals[j] = 2*((value - self.__min)/(self.__max - self.__min)) -1
                    j += 1
            i = i+1

    # index is the position referred to the single band
    def getGain(self, index):
        return self.__gainVals[index]