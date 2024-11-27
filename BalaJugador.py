import pygame

from resources.Colors import *


class BalaJugador:
    def __init__(self, x, y):
        self.imagen = pygame.image.load("resources/imagenBala.png")  # Cargar la imagen de la bala

        self.imagen = pygame.transform.scale(self.imagen, (20, 40)) # Redimensionar la imagen

        self.rect = self.imagen.get_rect(center=(x, y))  # Obtener el rectángulo de la bala

    def mover(self):
        self.rect.y -= 3  # Velocidad del proyectil hacia arriba

    def dibujar(self, superficie):
        superficie.blit(self.imagen, self.rect)
        #pygame.draw.rect(superficie, WHITE, self.rect)  # Dibuja el proyectil en blanco