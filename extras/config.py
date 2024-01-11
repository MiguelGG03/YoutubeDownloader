from pathlib import Path

AUDIO_OPTS = {
    'baja': {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '96',  # Baja calidad
        }],
    },
    'media': {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '128',  # Calidad media
        }],
    },
    'alta': {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',  # Alta calidad
        }],
    },
}


VIDEO_OPTS = {
    'alta': {
        'format': 'bestvideo+bestaudio/best',  # Descarga la mejor calidad de video y audio
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4',  # Convertir a mp4 si es necesario
        }],
    },
    'media': {
        'format': 'bestvideo+bestaudio/best',  # Descarga la mejor calidad de video y audio
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4',  # Convertir a mp4 si es necesario
        }],
    },
    'baja': {
        'format': 'bestvideo+bestaudio/best',  # Descarga la mejor calidad de video y audio
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4',  # Convertir a mp4 si es necesario
        }],
    },
}

PATH = Path.cwd()
PATH_DESCARGAS = PATH / 'descargas'
RUTA_DESCARGAS = str(PATH_DESCARGAS / "%(title)s.%(ext)s")