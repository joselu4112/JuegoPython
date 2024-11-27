import pygame
import sys
from PIL import Image

class Gif:
    """Clase con todos los metodos necesarios para cargar el gif de derrota de enemigo"""
    def __init__(self, ruta, screen, velocidad=15 ):
        #Parametros generales
        self.ruta = ruta #Ruta del gif
        self.screen = screen #Pantalla donde se va a pintar
        self.velocidad = velocidad  #velocidad de fotogramas
        self.frames = []    #Lista con los diferentes frames
        self.frame_index = 0    #Frame que se va a mostrar
        self.frame_count = 0    #Total de frames
        self.se_va_a_ver = False    #Para controlar cuando debe dibujarse
        self.x=0    #Pocicion (x,y) donde se va a dibujar, el target seria que se dibuje sobre el enemigo muerto
        self.y=0
        self.cargar_frames() #Cargamos los frames

    def cargar_frames(self):
        """
        Carga todos los fotogramas del GIF usando Pillow y los convierte en objetos de imagen para Pygame.
        """

        gif = Image.open(self.ruta) #Cargar la primera imagen

        try:
            while True: #Bucle para alternar los gift
                # Redimensionar el gif porque salia gigante
                gif_resized = gif.resize((100, 100),Image.Resampling.LANCZOS)

                # Convertir cada fotograma a formato RGB y cargarlo en Pygame
                frame = pygame.image.fromstring(gif_resized.convert('RGB').tobytes(), (100,100), 'RGB')

                self.frames.append(frame)#Añadimos el frame a la lista

                self.frame_count += 1#Lo sumamos

                gif.seek(gif.tell() + 1)  # Avanzar al siguiente fotograma
        except EOFError:
            pass  # Fin del GIF porque no hay mas fotogramas, esto lanzará la excepcion EOFError que aqui controlo


    def mostrar(self):
        """Metodo para controlar que se muestre en la siguiente iteracion del bucle del juego"""
        self.se_va_a_ver= True

    def ocultar(self):
        """Detiene la animación y reinicia el GIF."""
        self.frame_index = 0 #Reiniciar el gif a la posicion 0
        self.se_va_a_ver= False

    def setPosicion(self,x,y):
        """Metodo para indicar en que posicion va a mostrarse el gif"""
        self.x=x
        self.y=y
    
    def dibujar(self):
        """Dibuja el GIF en la pantalla de Pygame."""
        if self.se_va_a_ver: #Si hemos seleccionado que se mostrara

            # Dibujar el fotograma actual en la pantalla
            self.screen.blit(self.frames[self.frame_index], (self.x, self.y))

            pygame.display.flip()  # Actualiza la pantalla
            pygame.time.delay(self.velocidad)  # Controla el tiempo entre fotogramas

            # Avanzar al siguiente fotograma, con el operador modulo vuelve a 0 cuando muestra todos los fotogramas
            self.frame_index = (self.frame_index + 1) % self.frame_count

            if self.frame_index == 0:  # Cuando hemos vuelto al primer fotograma
                self.ocultar() #Metodo ocultar
