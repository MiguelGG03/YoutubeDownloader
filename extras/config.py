from pathlib import Path

AUDIO_OPTS = {
    
    '96kbps': {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '96',  # Baja calidad
        }],
        'writethumbnail': True,
    },
    
    '128kbps': {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '128',  # Calidad media
        }],
        'writethumbnail': True,
    },
    
    '192kbps': {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',  # Alta calidad
        }],
        'writethumbnail': True,
    },
    
    '256kbps': {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '256kbps',  # Alta calidad
        }],
        'writethumbnail': True,
    },
    
    '320kbps': {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320',  # Alta calidad
        }],
        'writethumbnail': True,
    },
}


VIDEO_OPTS = {
    
    '480p': {
        'format': 'bestvideo[height<=480]+bestaudio',  # Descarga la mejor calidad de video y audio
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4',  # Convertir a mp4 si es necesario
        }],
        'writethumbnail': True,
    },
    
    '720p': {
        'format': 'bestvideo[height<=720]+bestaudio',  # Descarga la mejor calidad de video y audio
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4',  # Convertir a mp4 si es necesario
        }],
        'writethumbnail': True,
    },
    
    '1080p': {
        'format': 'bestvideo[height<=1080]+bestaudio',  # Descarga la mejor calidad de video y audio
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4',  # Convertir a mp4 si es necesario
        }],
        'writethumbnail': True,
    },
    
    '1440p': {
        'format': 'bestvideo[height<=1440]+bestaudio',  # Descarga la mejor calidad de video y audio
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4',  # Convertir a mp4 si es necesario
        }],
        'writethumbnail': True,
    },
    
    '4k': {
        'format': 'bestvideo[height<=2160]+bestaudio',  # Descarga la mejor calidad de video y audio
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4',  # Convertir a mp4 si es necesario
        }],
        'writethumbnail': True,
    },
}

PATH = Path.cwd()
PATH_DESCARGAS = PATH / 'descargas'
RUTA_DESCARGAS = str(PATH_DESCARGAS / "%(title)s.%(ext)s")