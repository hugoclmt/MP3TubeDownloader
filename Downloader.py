import yt_dlp as youtube_dl
import os

class Downloader:

    def __init__(self):
        self.__chemin = "C:\\elliot"  # Utilisez des doubles barres obliques inverses pour Windows

    def download(self, urlDeLaVideo, progress_callback):
        if(urlDeLaVideo != "") and (isinstance(urlDeLaVideo, str)):    
            ydl_opts = {
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
                'outtmpl': os.path.join(self.__chemin, '%(title)s.%(ext)s'),
                'progress_hooks': [progress_callback],
            }

            try:
                with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([urlDeLaVideo])
                print("Téléchargement et conversion terminés")
            except Exception as e:
                print(f"Erreur: {e}")
        else:
            raise ValueError("L'URL de la vidéo ne peut pas être vide et doit être une chaîne de caractères")
