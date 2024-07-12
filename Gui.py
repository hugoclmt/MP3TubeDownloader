from tkinter import *
from Downloader import *
import threading
from tkinter import ttk

class Gui:
    def __init__(self, master):
        self.master = master
        self.download = Downloader()
        self.master.title("Convertisseur MP3 on YouTube")
        self.master.geometry("500x300")
        self.label = Label(self.master, text="Entrez l'URL de la vidéo YouTube")
        self.label.pack(pady=10)
        self.entry = Entry(self.master,width=50)
        self.entry.pack(pady=10)
        self.button = Button(self.master, text="Télécharger", command=self.onclick_button)
        self.button.pack(pady=10)
        self.progress = Label(self.master, text="")
        self.progress.pack()
        self.progressbar = ttk.Progressbar(self.master, orient='horizontal', mode='determinate', length=400)
        self.progressbar.pack(pady=10)

    def onclick_button(self):
        url = self.entry.get()
        self.progressbar['value'] = 0
        threading.Thread(target=self.start_download, args=(url,)).start()

    def start_download(self, url):
        self.download.download(url, self.progress_callback)
        self.entry.delete(0, END)

    def progress_callback(self, d):
        if d['status'] == 'downloading':
            total_bytes = d.get('total_bytes') or d.get('total_bytes_estimate')
            if total_bytes:
                percent = d['downloaded_bytes'] / total_bytes * 100
                self.progressbar['value'] = percent
                self.progress['text'] = f"Téléchargement : {percent:.2f}%"
        elif d['status'] == 'finished':
            self.progress['text'] = "Téléchargement terminé !"
            self.progressbar['value'] = 100