import tkinter as tk

class Gain:
	def __init__(self, root):

		self.scale = tk.Scale(master=root, 
					  		  orient=tk.VERTICAL,
					  		  digits=2,
					  		  showvalue=0,
					  		  length=200, 
					  		  from_=12.0, 
					  		  to=-12.0)

		# show up
		self.scale.pack(fill=tk.BOTH)