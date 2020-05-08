import tkinter as tk
import tkinter.ttk as ttk

DARK_COLOR = '#2D2D2D'

class Switcher:

	def __init__(self, root, r, c):
		self.active = ttk.Checkbutton(root, text='Active')
		self.preset = ttk.Combobox(root, textvariable='hello')

		self.active.grid(row=r, column=c, columnspan=2, pady=10)
		self.preset.grid(row=r, column=c+3, columnspan=5, pady=10)