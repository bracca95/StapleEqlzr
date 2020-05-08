import tkinter as tk

DARK_COLOR = '#2D2D2D'

class Gain:
	def __init__(self, root, r, c):

		self.scale = tk.Scale(master=root, 
					  		  orient=tk.VERTICAL,
					  		  digits=2,
					  		  showvalue=0,
					  		  length=200, 
					  		  from_=12.0, 
					  		  to=-12.0,
					  		  highlightcolor=DARK_COLOR)

		# show up
		self.scale.grid(row=r, column=c, padx=10, rowspan=3)