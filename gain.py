import tkinter as tk

class Gain:
	def __init__(self, root, gainKey):

		self.gains = {
		'1': '32', '2': '64', '3': '125', '4': '250', '5': '500', '6': '1k',
		'7': '2k', '8': '4k', '9': '8k', '10': '16k'
		}

		self.scale = tk.Scale(master=root, 
					  		  orient=tk.VERTICAL,
					  		  digits=2,
					  		  showvalue=0,
					  		  length=200, 
					  		  from_=12.0, 
					  		  to=-12.0)

		self.label = tk.Label(master=root, text=self.gains[gainKey])

		# show up
		self.scale.grid(row=0, column=0, padx=10)
		self.label.grid(row=2, column=0, pady=10)