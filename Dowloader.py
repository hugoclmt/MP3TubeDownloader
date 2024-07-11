import yt_dlp as youtube_dl
import os

class Downloader:

    def __init__(self):
        self.__chemin = "C:\\elliot"  # Utilisez des doubles barres obliques inverses pour Windows

    def dowload(self, urlDeLaVideo):
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'outtmpl': os.path.join(self.__chemin, '%(title)s.%(ext)s'),
        }

        try:
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([urlDeLaVideo])
            print("Téléchargement et conversion terminés")
        except Exception as e:
            print(f"Erreur: {e}")

