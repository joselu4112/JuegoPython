import pygame
import sys

from juegoPrincipal import juego


class MenuPrincipal:

    #Menu principal de el juego, clase donde inicia.

    #Contiene una imagen de fondo el y botones de jugar y salir

    def __init__(self, pantalla, ancho, alto):
        # Inicialización de las variables de este
        self.pantalla = pantalla
        self.ancho = ancho
        self.alto = alto
        self.fuente = pygame.font.SysFont("Arial", 30)

        # Cargar la imagen de fondo
        self.fondo = pygame.image.load("resources/espacio.gif")
        self.fondo = pygame.transform.scale(self.fondo, (self.ancho, self.alto))

        # Crear los botones
        self.boton_jugar = pygame.Rect(self.ancho // 2 - 100, self.alto // 2 - 50, 200, 50)
        self.boton_salir = pygame.Rect(self.ancho // 2 - 100, self.alto // 2 + 20, 200, 50)

    def dibujar_boton(self, texto, rect, color):
        """Dibuja un botón con el texto y el color indicado"""
        pygame.draw.rect(self.pantalla, color, rect)
        texto_renderizado = self.fuente.render(texto, True, (0, 0, 0))
        self.pantalla.blit(texto_renderizado, (
        rect.centerx - texto_renderizado.get_width() // 2, rect.centery - texto_renderizado.get_height() // 2))

    def mostrar(self):
        """Muestra el menú principal y gestiona los eventos de los 2 botones"""
        while True:
            for event in pygame.event.get():
                #Salir del juego
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    #Boton de iniciar partida
                    if self.boton_jugar.collidepoint(event.pos):
                        print("Iniciar juego")
                        return  juego()#Llamamos al metodo juego de la clase juegoPrincipal
                    #Boton de salir
                    elif self.boton_salir.collidepoint(event.pos):
                        pygame.quit()
                        sys.exit()

            # Dibujar la imagen de fondo
            self.pantalla.blit(self.fondo, (0, 0))

            # Dibujar los botones
            self.dibujar_boton("Jugar", self.boton_jugar, (243, 231, 54))  # Botón verde para "Jugar"
            self.dibujar_boton("Salir", self.boton_salir, (237, 61, 22))  # Botón rojo para "Salir"

            # Actualizar la pantalla
            pygame.display.update()


if __name__=='__main__':
    #Inicio del programa

    # Inicialización de Pygame
    pygame.init()

    # Dimensiones de la ventana
    ANCHO = 800
    ALTO = 600
    pantalla = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption("Menú Principal")

    # Crear una instancia de MenuPrincipal y mostrar el menú
    menu = MenuPrincipal(pantalla, ANCHO, ALTO)
    menu.mostrar()