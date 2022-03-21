from tkinter import *

class Convertor:
    def __init__(self, parent):
        print("hello world")

if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Convertor")
    something = Convertor(root)
    root.mainloop()
