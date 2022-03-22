from tkinter import *

class Convertor:
    def __init__(self, parent):
        background_color = "light blue"
        self.converter_frame = Frame(width=600, height=600, bg=background_color)
        self.converter_frame.grid()

        self.temp_converter_label = Label(text="Temperature Converter",
                                          font=("Ariel", "16", "bold"),
                                          bg=background_color,
                                          padx=10, pady=10)
        self.temp_converter_label.grid(row=0)

if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Convertor")
    something = Convertor(root)
    root.mainloop()
