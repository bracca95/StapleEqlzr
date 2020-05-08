import tkinter as tk

DARK_COLOR = '#2D2D2D'

class Band:
	def __init__(self, root, r, c, gainKey):

		self.gains = {
		'1': '32', '2': '64', '3': '125', '4': '250', '5': '500', '6': '1k',
		'7': '2k', '8': '4k', '9': '8k', '10': '16k'
		}

		self.label = tk.Label(master=root, text=self.gains[gainKey],
								fg='white', bg=DARK_COLOR)

		# show up
		self.label.grid(row=r, column=c, pady=5)