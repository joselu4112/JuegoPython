import pygame
import sys
from PIL import Image

class Gif:
    def __init__(self, ruta, screen, velocidad=15 ):
        """
        Inicializa la clase GIF con la ruta del archivo y la pantalla de Pygame donde se mostrará.
        :param ruta: Ruta del archivo GIF.
        :param screen: Objeto de la pantalla de Pygame donde se mostrará el GIF.
        :param velocidad: Retraso entre fotogramas en milisegundos.
        """
        self.ruta = ruta
        self.screen = screen
        self.velocidad = velocidad
        self.frames = []
        self.frame_index = 0
        self.frame_count = 0
        self.se_va_a_ver = False
        self.x=0
        self.y=0
        self.cargar_frames() #Cargamos los frames

    def cargar_frames(self):
        """
        Carga todos los fotogramas del GIF usando Pillow y los convierte en objetos de imagen para Pygame.
        """

        gif = Image.open(self.ruta)

        try:
            while True:
                # Redimensionar el gif porque salia gigante
                gif_resized = gif.resize((100, 100),Image.Resampling.LANCZOS)

                # Convertir cada fotograma a formato RGB y cargarlo en Pygame
                frame = pygame.image.fromstring(gif_resized.convert('RGB').tobytes(), (100,100), 'RGB')
                self.frames.append(frame)
                self.frame_count += 1
                gif.seek(gif.tell() + 1)  # Avanzar al siguiente fotograma
        except EOFError:
            pass  # Fin del GIF

    def mostrar(self):
        """Inicia la animación del GIF."""
        self.se_va_a_ver= True

    def ocultar(self):
        """Detiene la animación y reinicia el GIF."""
        self.frame_index = 0
        self.se_va_a_ver= False

    def setPosicion(self,x,y):
        self.x=x
        self.y=y
    
    def dibujar(self):
        """Dibuja el GIF en la pantalla de Pygame."""
        if self.se_va_a_ver:
            # Dibujar el fotograma actual en la pantalla
            self.screen.blit(self.frames[self.frame_index], (self.x, self.y))
            pygame.display.flip()  # Actualiza la pantalla
            pygame.time.delay(self.velocidad)  # Controla el tiempo entre fotogramas

            # Avanzar al siguiente fotograma, con el operador modulo vuelve a 0 cuando muestra todos los fotogramas
            self.frame_index = (self.frame_index + 1) % self.frame_count

            if self.frame_index == 0:  # Cuando hemos vuelto al primer fotograma
                self.ocultar()
