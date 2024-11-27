import pygame

from resources.Colors import *


class BalaJugador:
    """Clase BalaJugador, con la imagen de las balas de este y metodos para dibujarlas y moverlas."""
    def __init__(self, x, y):
        self.imagen = pygame.image.load("resources/imagenBala.png")  # Cargar la imagen de la bala

        self.imagen = pygame.transform.scale(self.imagen, (20, 40)) # Redimensionar la imagen

        self.rect = self.imagen.get_rect(center=(x, y))  # Obtener el rectángulo de la bala

    def mover(self):
        #Metodo para mover la bala
        self.rect.y -= 3  # Velocidad del proyectil hacia arriba

    def dibujar(self, superficie):
        #Metodo para pintar la bala
        superficie.blit(self.imagen, self.rect)