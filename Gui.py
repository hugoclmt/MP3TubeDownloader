from tkinter import *
from Dowloader import *


class Gui:
    def __init__(self, master):
        self.master = master
        self.download = Downloader()
        self.master.title("Convertisseur MP3 on YouTube")
        self.master.geometry("800x600")
        self.label = Label(self.master, text="Hello World")
        self.label.pack()
        self.button = Button(self.master, text="Close", command=self.master.quit)
        self.button.pack()