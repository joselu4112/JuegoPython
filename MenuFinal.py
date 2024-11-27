import pygame
import sys


class MenuFinal:
    #Menu semejante al MenuPrincipal pero en este caso para cuando la partida ha terminado con lo botones salir y volver a jugar

    def __init__(self, pantalla, ancho, alto, puntuacion):
        #Inicializar variables de la pantalla
        self.pantalla = pantalla
        self.ancho = ancho
        self.alto = alto
        self.puntuacion = puntuacion #Puntuacion del jugador que se la paso desde la clase juego principal al acabar este.
        self.fuente = pygame.font.SysFont("Arial", 30)

        # Cargar la imagen de fondo
        self.fondo = pygame.image.load("resources/espacio.gif")
        self.fondo = pygame.transform.scale(self.fondo, (self.ancho, self.alto))

        # Crear los botones de volver a jugar y salir
        self.boton_jugar = pygame.Rect(self.ancho // 2 - 100, self.alto // 2, 200, 50)
        self.boton_salir = pygame.Rect(self.ancho // 2 - 100, self.alto // 2 + 70, 200, 50)

    def dibujar_boton(self, texto, rect, color):
        """Dibuja un botón con el texto y el color indicado"""
        pygame.draw.rect(self.pantalla, color, rect)
        texto_renderizado = self.fuente.render(texto, True, (0, 0, 0))
        self.pantalla.blit(texto_renderizado, (
        rect.centerx - texto_renderizado.get_width() // 2, rect.centery - texto_renderizado.get_height() // 2))

    def mostrar(self):
        """Muestra el menú final y gestiona los eventos"""
        while True:
            for event in pygame.event.get():
                #Si se cierra la pantalla se cierra
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    #Dibujar los botones
                    if self.boton_jugar.collidepoint(event.pos):
                        #Boton volver a jugar
                        print("Volver a jugar")
                        return  True
                    elif self.boton_salir.collidepoint(event.pos):
                        #Boton salir
                        pygame.quit()
                        sys.exit()
                        return False

            # Dibujar la imagen de fondo
            self.pantalla.blit(self.fondo, (0, 0))

            # Mostrar la puntuacion total obtenida
            texto_puntuacion = self.fuente.render(f"Puntuación: {self.puntuacion}", True, (255, 255, 255))
            self.pantalla.blit(texto_puntuacion,
                               (self.ancho // 2 - texto_puntuacion.get_width() // 2, self.alto // 2 - 100))

            # Dibujar los botones
            self.dibujar_boton("Volver a jugar", self.boton_jugar, (243, 231, 54))  # Botón verde
            self.dibujar_boton("Salir", self.boton_salir, (237, 61, 22))  # Botón rojo

            # Actualizar la pantalla
            pygame.display.update()