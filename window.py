import tkinter as tk
import tkinter.ttk as ttk
from gain import Gain

## CONSTANTS
DARK_COLOR = '#2D2D2D'
NUM_SLIDER = 10
#WIN_WIDTH = 600
#WIN_HEIGHT = 300
#SCREEN_RES = str(WIN_WIDTH)+'x'+str(WIN_HEIGHT)

class Window(tk.Tk):

	def __init__(self):
		tk.Tk.__init__(self)

		# aspect and configuration
		#self.geometry(SCREEN_RES)					# aspect ratio
		self.title('Staple Eqlz')					# window title
		self.resizable(False, False)				# lock width, height
		self.configure(background=DARK_COLOR)		# background colour

		# divide space in frames
		# num slider + space for labels
		for i in range(NUM_SLIDER+1):
			self.frame = tk.Frame(self,
								  background='yellow',
								  relief=tk.GROOVE,
								  borderwidth=5)

			# show
			if i < 1:
				self.frame.grid(row=0, column=i)
				self.labp12 = tk.Label(self.frame, text='+12 dB').grid(row=0, column=i, pady=50)
				self.labnul = tk.Label(self.frame, text='0 dB').grid(row=1, column=i, pady=50)
				self.labm12 = tk.Label(self.frame, text='-12 dB').grid(row=2, column=i, pady=50)
			else:
				self.frame.grid(row=0, column=i, pady=50)
				self.gain = Gain(self.frame, str(i))