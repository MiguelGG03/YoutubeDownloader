import sys
from abc import ABC, abstractmethod
from pathlib import Path

# Añade el directorio raíz del proyecto a sys.path
# Esto asume que este archivo está en la subcarpeta 'clases' del proyecto

root_path = Path(__file__).resolve().parent.parent
sys.path.append(str(root_path))

from extras.config import AUDIO_OPTS, VIDEO_OPTS

# Clase abstracta base para definir calidades de audio y video.
class Quality(ABC):
    
    def __init__(self):
        self.dictionary = None  # Diccionario para almacenar las opciones de calidad.
        self.quality = None  # Opción de configuración correspondiente a la calidad seleccionada.
        try:
            self.setDictionary()  # Intenta definir el diccionario de calidad.
        except:
            pass  # Si hay un error al definir el diccionario, lo ignora.
        
    def setQuality(self,selection):
        # Establece la calidad de audio basada en la selección del usuario.
        # Convierte la selección numérica en una calidad de audio (baja, media, alta).
        lista = []
        try:
            selection = int(selection)
            selection -= 1
        except:
            print(f"Error: {selection} no es una opción válida (necesariamente int) .")    
        
        for name in self.dictionary:
            lista.append(name)
            
        if selection < 0 or selection > len(lista) - 1:
            print(f"Error: {selection} no es una opción válida (fuera de rango).")
        else:
            self.quality = self.dictionary[lista[selection]]
            print(f"Se ha seleccionado la calidad {lista[selection]}")

        
    @abstractmethod
    def qualityPrinter(self):
        # Método abstracto para imprimir las opciones de calidad.
        pass
        
    @abstractmethod
    def setDictionary(self):
        # Método abstracto para establecer el diccionario de opciones de calidad.
        pass
    
    
# Subclase concreta de Quality para calidades de audio.
class AudioQuality(Quality):
    
    def setDictionary(self):
        # Define el diccionario de opciones de calidad de audio.
        self.dictionary = AUDIO_OPTS
                
    def qualityPrinter(self):
        # Imprime las opciones de calidad de audio disponibles.
        counter = 1
        print()
        for a in self.dictionary:
            print(f"{counter}. {a} :")
            # Imprime detalles de la configuración de calidad de audio.
            print(f"    · format :  {self.dictionary[a]['format']}")
            print(f"    · postprocessors :")
            print(f"       - key : {self.dictionary[a]['postprocessors'][0]['key']}")
            print(f"       - preferredcodec : {self.dictionary[a]['postprocessors'][0]['preferredcodec']}")
            print(f"       - preferredquality : {self.dictionary[a]['postprocessors'][0]['preferredquality']}")
            print()
            counter += 1

# Subclase concreta de Quality para calidades de video.
class VideoQuality(Quality):
    
    def setDictionary(self):
        # Define el diccionario de opciones de calidad de video.
        self.dictionary = VIDEO_OPTS
            
    def qualityPrinter(self):
        # Imprime las opciones de calidad de video disponibles.
        counter = 1
        print()
        for a in self.dictionary:
            print(f"{counter}. {a} :")
            # Imprime detalles de la configuración de calidad de video.
            print(f"    · format :  {self.dictionary[a]['format']}")
            print(f"    · postprocessors :")
            print(f"       - key : {self.dictionary[a]['postprocessors'][0]['key']}")
            print(f"       - preferedformat : {self.dictionary[a]['postprocessors'][0]['preferedformat']}")
            print()
            counter += 1


