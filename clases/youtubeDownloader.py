import yt_dlp
import sys
from pathlib import Path
from quality import AudioQuality, VideoQuality

root_path = Path(__file__).resolve().parent.parent
sys.path.append(str(root_path))

from extras.config import PATH_DESCARGAS

class YoutubeDownloader:
    def __init__(self):
        self.url = input("Enter the URL of the video you want to download: ")
        self.quality = {}        

    def setVideoQuality(self,selecction):
        v = VideoQuality()
        v.qualityPrinter()
        v.setQuality(selecction)
        self.quality = v.quality
        self.setDestinyFolder()
        
    def setAudioQuality(self,selection):
        a = AudioQuality()
        a.qualityPrinter()
        a.setQuality(selection)
        self.quality = a.quality
        self.setDestinyFolder()

    def setDestinyFolder(self):
        self.quality["outtmpl"] = str(PATH_DESCARGAS / "%(title)s.%(ext)s")

    def download(self):
        # Get the best audio possible
        with yt_dlp.YoutubeDL(self.quality) as ydl:
            ydl.download([self.url])
            
if __name__ == "__main__":
    y = YoutubeDownloader()
    s = "3"
    y.setAudioQuality(s)
    y.download()