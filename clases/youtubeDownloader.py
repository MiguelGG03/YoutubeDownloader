import yt_dlp
from pathlib import Path
from quality import AudioQuality, VideoQuality
import sys

root_path = Path(__file__).resolve().parent.parent
sys.path.append(str(root_path))

from extras.config import PATH_DESCARGAS

class YoutubeDownloader:
    def __init__(self):
        self.url = input("Enter the URL of the video you want to download: ")
        self.quality = {}
        self.destinyFolder = str(PATH_DESCARGAS / "%(title)s.%(ext)s")
        
    def setDestinyFolder(self,newPath = None):
        if newPath == None:
            self.destinyFolder = str(PATH_DESCARGAS / "%(title)s.%(ext)s")
        else:
            self.destinyFolder = newPath

    def setVideoQuality(self,selecction):
        v = VideoQuality()
        v.qualityPrinter()
        v.setQuality(selecction)
        self.quality = v.quality
        
    def setAudioQuality(self,selection):
        a = AudioQuality()
        a.qualityPrinter()
        a.setQuality(selection)
        self.quality = a.quality
        
    def download(self):
        self.quality['outtmpl'] = self.destinyFolder
        with yt_dlp.YoutubeDL(self.quality) as ydl:
            ydl.download([self.url])
            
            
if __name__ == "__main__":
    y = YoutubeDownloader()
    y.setAudioQuality("3")
    y.download()