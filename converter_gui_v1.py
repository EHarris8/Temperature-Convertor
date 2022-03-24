from tkinter import *
from functools import partial
import random

class Converter:
    def __init__(self):

        #formatting variables
        background_color = "light blue"

        #converter frame
        self.converter_frame = Frame(width=300, bg=background_color,
                                     pady=10)
        self.converter_frame.grid()

        #temperature converter heading
        self.temp_heading_label = Label(self.converter_frame,
                                        text = "Temperature Converter",
                                            font="Arial 16 bold",
                                            bg=background_color,
                                            padx=10, pady=10)
        self.temp_heading_label.grid(row=0)

        #user instructions
        self.temp_instructions_label = Label(self.converter_frame,
                                             text = "Type in the amount to be "
                                                     "converted and then push "
                                                     "one of the buttons below...",
                                                     font="Arial 10 italic", wrap=250,
                                                     justify=LEFT, bg=background_color,
                                                     padx=10, pady=10)
        self.temp_instructions_label.grid(row=1)
        
        
