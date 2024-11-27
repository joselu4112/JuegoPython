import math

import pygame

from resources.Colors import *


class Enemigo1:
    def __init__(self, targetx, targety, salud,danio, x, y):
        self.distancia=None
        self.vector_x=None
        self.vector_y=None

        self.posx=x
        self.posy=y
        self.salud = salud
        self.puntos=10
        self.danio=danio
        self.saludInicial=salud
        self.targetx=targetx
        self.targety=targety
        self.velocidad=1

        self.ruta="resources/enemigo.png" #Enemigo base

        if(self.danio>=10):#Enemigo con mas daño
            self.ruta="resources/fotoDaño.jpg"
        if(self.salud>=550):#Enemigo con mas vida
            self.ruta = "resources/fotoVida.jpeg"
        if(self.salud>=550 and self.danio>=10):#Enemigo con vida y daño altos
            self.ruta = "resources/toptop.jpg"
        if(self.salud==800):#Enemigo con top vida
            self.ruta = "resources/TopVida.jpg"
        if (self.danio == 20):#Enemigo con top daño
            self.ruta = "resources/TopDanio.jpg"
        if(self.danio==20 and self.salud==800):#Enemigo TopTop
            self.ruta = "resources/Topjiafei.jpg"

        self.imagen = pygame.image.load(self.ruta)
        self.imagen = pygame.transform.scale(self.imagen, (80, 80))  # Redimensionar
        self.rect = self.imagen.get_rect(center=(self.posx, self.posy))


    def setPosicionInicial(self,x,y):
        #Distancia a 0 para calcularla despues
        self.distancia=0
        #Nueva posicion de destino
        self.posx = x
        self.rect.x = x

        self.posy = y
        self.rect.y = y

        # Calculo de la distancia al punto de destino
        self.vector_x = self.targetx - self.posx
        self.vector_y = self.targety - self.posy
        self.distancia = math.sqrt(self.vector_x ** 2 + self.vector_y ** 2)


    def setTarget(self,targetx,targety):
        self.targetx=targetx
        self.targety=targety

        # Calculo de la distancia al nuevo punto de destino
        self.vector_x = self.targetx - self.posx
        self.vector_y = self.targety - self.posy

        self.distancia = math.sqrt(self.vector_x ** 2 + self.vector_y ** 2)



    def dibujar(self, superficie):
            superficie.blit(self.imagen, self.rect)  # Dibujar la imagen del enemigo
            self.dibujar_barra_vida(superficie)  # Dibujar la barra de vida

    def dibujar_barra_vida(self, superficie):
        # Barra de vida
        vida_ancho = 50  # Ancho de la barra de vida
        vida_alto = 5    # Alto de la barra de vida
        porcentaje_vida = self.salud / self.saludInicial  # Suponiendo que la salud máxima es 100
        pygame.draw.rect(superficie, RED, (self.rect.x, self.rect.y - 10, vida_ancho, vida_alto))  # Fondo
        pygame.draw.rect(superficie, GREEN, (self.rect.x, self.rect.y - 10, vida_ancho * porcentaje_vida, vida_alto))  # Vida actual

    def recibir_dano(self, dano):
        self.salud -= dano
        if self.salud < 0:
            self.salud = 0  # No permitir que la salud sea negativa


    def animar(self):
        if self.distancia != 0:
            #Calculo el vector normalizado
            self.dx_normalizado = self.vector_x / self.distancia
            self.dy_normalizado = self.vector_y / self.distancia

    def mover(self):
            #Calculo el movimiento como el vector normalizado por la velocidad
            self.posx += self.dx_normalizado * self.velocidad
            self.posy += self.dy_normalizado * self.velocidad
            #Actualizo su rect para que se dibuje en la posicion deseada
            self.rect.x = self.posx
            self.rect.y = self.posy
            # Calculo de la nueva distancia al punto de destino
            self.vector_x = self.targetx - self.posx
            self.vector_y = self.targety - self.posy
            self.distancia = math.sqrt(self.vector_x ** 2 + self.vector_y ** 2)