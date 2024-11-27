import math

import pygame
from resources.Colors import RED

class BalaEnemigo:
    """"Clase que define el movimiento y animacion de las balas de los enemigos"""
    #Las Balas de los enemigos se mueven hacia el jugador en linea recta, este donde este en la pantalla apuntan siempre a el.

    def __init__(self, x, y, targetx,targety,velocidad=2):
        #Posicion inicial, la posicion del enemigo en el momento de disparo
        self.x = x
        self.y = y

        self.imagen = pygame.image.load("resources/pelota.png")  # Cargar la imagen de la bala

        self.imagen = pygame.transform.scale(self.imagen, (40, 40))  # Redimensionar la imagen

        self.rect = self.imagen.get_rect(center=(x, y))  # Obtener el rectángulo de la bala

        self.velocidad=velocidad #Velocidad

        #Posicion a donde apunta la bala, en este caso la posicion del jugador en el momento de disparo
        self.targetx=targetx
        self.targety=targety

        # Calcular la dirección hacia el objetivo
        dx = targetx - self.x
        dy = targety - self.y

        # Calcular la distancia total
        distancia = math.sqrt(dx ** 2 + dy ** 2)

        # Normalizar el vector (dx, dy) para obtener la dirección
        if distancia != 0:
            self.dx_normalizado = dx / distancia
            self.dy_normalizado = dy / distancia

    def dibujar(self, superficie):
        #Metodo para dibujar la bala enemigo en la superficie
        superficie.blit(self.imagen, self.rect)

    def mover(self):
        #Metodo para mover la bala

        # Mover la bala en la dirección calculada
        self.x += self.dx_normalizado * self.velocidad
        self.y += self.dy_normalizado * self.velocidad

        # Actualizar el rectángulo para que coincida con la nueva posición
        self.rect.x = self.x
        self.rect.y = self.y
