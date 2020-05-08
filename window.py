import tkinter as tk
import tkinter.ttk as ttk
from gain import Gain

## CONSTANTS
DARK_COLOR = '#2D2D2D'
NUM_SLIDER = 10
WIN_WIDTH = 600
WIN_HEIGHT = 300
SCREEN_RES = str(WIN_WIDTH)+'x'+str(WIN_HEIGHT)

class Window(tk.Tk):

	def __init__(self):
		tk.Tk.__init__(self)

		# aspect and configuration
		self.geometry(SCREEN_RES)					# aspect ratio
		self.title('Staple Eqlz')					# window title
		self.resizable(False, False)				# lock width, height
		self.configure(background=DARK_COLOR)		# background colour

		# divide space in frames
		# num slider + space for labels
		for i in range(NUM_SLIDER+1):
			self.frame = tk.Frame(self,
								  width=WIN_WIDTH/(NUM_SLIDER+1),
								  height=200,
								  background='yellow',
								  relief=tk.GROOVE,
								  borderwidth=5)

			# 
			#self.gain = Gain(self.frame)

			# show
			self.frame.grid(row=10, column=i, sticky='S')