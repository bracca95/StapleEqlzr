# Description
Simple implementation of a 10-band graphic equalizer with FIR filters by truncation. The program currently takes as input a sample song in `media/` and returns the equalized song in the main project directory, which can be played with any media player.
In order to choose the preset: go to the `main.py` and change a numeric value (int). To see and edit preset, use the `utilities/presets.txt` file

There are still things to do:
- save both audio channels
- draw a GUI
- play "on the fly"
- custom presets

# References
1 integrated GUI
- https://youtu.be/2vWCzB9HBgk

2 pysoundfile
- https://pypi.org/project/PySoundFile/ 
- https://pysoundfile.readthedocs.io/en/0.9.0/

3 audioread
- https://pypi.org/project/audioread/

4 pydub
- https://github.com/jiaaro/pydub
- https://github.com/jiaaro/pydub/blob/master/API.markdown
- https://stackoverflow.com/a/43950755

5 bytes to int
- https://stackoverflow.com/questions/34009653/convert-bytes-to-int
- https://www.delftstack.com/howto/python/how-to-convert-bytes-to-integers/
