import tkinter as tk
from switcher import Switcher
from gain import Gain
from band_labels import Band

## CONSTANTS
DARK_COLOR = '#2D2D2D'
NUM_SLIDER = 10
ROWS = 5
COLUMNS = 11

class Window(tk.Tk):

	def __init__(self):
		tk.Tk.__init__(self)

		# aspect and configuration
		self.title('Staple Eqlz')					# window title
		self.resizable(False, False)				# lock width, height
		self.configure(background=DARK_COLOR)		# background colour

		for row in range(ROWS):
			for col in range(COLUMNS):
				self.frame = tk.Frame(self).grid(row=row, column=col)

				if row == 0 and col == 1:
					self.active = Switcher(self.frame, row, col)

				if row == 1 and col == 0:
					self.labp12 = tk.Label(self.frame, text='+12 dB',
											fg='white', bg=DARK_COLOR)
					self.labp12.grid(row=row, column=col, padx=7)

				if row == 2 and col == 0:
					self.labnul = tk.Label(self.frame, text='0 dB',
											fg='white', bg=DARK_COLOR)
					self.labnul.grid(row=row, column=col, padx=7, pady=67)

				if row == 3 and col == 0:
					self.labm12 = tk.Label(self.frame, text='-12 dB',
											fg='white', bg=DARK_COLOR)
					self.labm12.grid(row=row, column=col, padx=7)

				if row == 1 and col > 0:
					self.gain = Gain(self.frame, row, col)

				if row == 4 and col > 0:
					self.band_lab = Band(self.frame, row, col, str(col))