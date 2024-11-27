import math

import pygame

from resources.Colors import *


class Enemigo1:
    """Clase enemigo, encargada de todas las interacciones con este y guardar sus valores aleatorios."""

    def __init__(self, targetx, targety, salud,danio, x, y):
        #Aqui inicializo nulas las variables que se calculan a partir de otras en metodos más adelante.
        self.distancia=None
        self.vector_x=None
        self.vector_y=None

        #Posicion inicial
        self.posx=x
        self.posy=y

        self.salud = salud #Vida en tiempo real
        self.danio=danio    #Daño
        self.saludInicial=salud #Vida inicial para pintar la barra de vida
        self.velocidad=1 #Velocidad de movimiento para las animaciones

        #Siguiente posicion a la que se debe mover el enemigo,
        # principalmente el movimiento una vez ha muerto y se genera un nuevo enemigo
        self.targetx=targetx
        self.targety=targety

        #Puntos que da este enemigo
        self.puntos=salud+danio*40
        #Dado que la generacion de daño es bastante mas pequeña en escala a la vida, para que la cantidad de puntos que dan
        #los enemigos con mas daño se multiplica por 40 para igualarlo a los que tienen más vida.

        #Diferntes enemigos que se presentan al usuario según los parametros aleatorios que se han generado.
        #Foto del enemigo base
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
        if(self.danio==20 and self.salud==800):#Enemigo Top to-do
            self.ruta = "resources/Topjiafei.jpg"

        self.imagen = pygame.image.load(self.ruta)#Cargar imagen seleccionada
        self.imagen = pygame.transform.scale(self.imagen, (80, 80))  # Redimensionar
        self.rect = self.imagen.get_rect(center=(self.posx, self.posy)) #Asignar el rect


    def setPosicionInicial(self,x,y):
        """Metodo para seleccionar la posicion inicial del enemigo.
        Se usa cuando muere un enemigo y quiero generar uno nuevo en la misma posicion para que este se mueva
        con una animacion a la posicion aleatoria generada Target(targetx, targety) """
        #Distancia a 0 para calcularla despues
        self.distancia=0

        #Nueva posicion Inicial
        self.posx = x
        self.rect.x = x

        self.posy = y
        self.rect.y = y

        # Calculo de la distancia al punto de destino segun esta nueva posicion inicial
        self.vector_x = self.targetx - self.posx
        self.vector_y = self.targety - self.posy
        self.distancia = math.sqrt(self.vector_x ** 2 + self.vector_y ** 2)


    def setTarget(self,targetx,targety):
        """Metodo para seleccionar una nueva posicion a la que mover el enemigo"""
        #Nuevo Target(targetx, targety)
        self.targetx=targetx
        self.targety=targety

        # Calculo de la distancia al nuevo punto de destino
        self.vector_x = self.targetx - self.posx
        self.vector_y = self.targety - self.posy

        self.distancia = math.sqrt(self.vector_x ** 2 + self.vector_y ** 2)



    def dibujar(self, superficie):
        """Metodo para dibujar al enemigo y su barra de vida"""
        superficie.blit(self.imagen, self.rect)  # Dibujar la imagen del enemigo
        self.dibujar_barra_vida(superficie)  # Dibujar la barra de vida

    def dibujar_barra_vida(self, superficie):
        # Barra de vida
        vida_ancho = 50  # Ancho de la barra de vida
        vida_alto = 5    # Alto de la barra de vida

        # Calculo del porcentaje de vida para ir porcentualmente reduciendo
        # el tamaño de la barra verde, de forma que la vida que falta se muestra en rojo
        porcentaje_vida = self.salud / self.saludInicial

        # Fondo rojo
        pygame.draw.rect(superficie, RED, (self.rect.x, self.rect.y - 10, vida_ancho, vida_alto))
        # Vida actual
        pygame.draw.rect(superficie, GREEN, (self.rect.x, self.rect.y - 10, vida_ancho * porcentaje_vida, vida_alto))

    def recibir_dano(self, dano):
        """Metodo para que el enemigo reciva daño"""
        self.salud -= dano
        if self.salud < 0:
            self.salud = 0  # No permitir que la salud sea negativa


    def animar(self):
        """Metodo para calcular el vector normalizado de direccion
        hacia el Target(targerx,targety) desde la posicion inicial(x,y)"""

        if self.distancia != 0:#Si no se encuentra ya en la posicion de destino (Que la distancia a Target sea 0)
            #Calculo el vector normalizado
            self.dx_normalizado = self.vector_x / self.distancia
            self.dy_normalizado = self.vector_y / self.distancia

    def mover(self):
        """Metodo que calcula las distancias y vectores necesarios
        para definir el movimiento desde la Posicion Inicial al Target"""
        #Calculo el movimiento como el vector normalizado por la velocidad
        self.posx += self.dx_normalizado * self.velocidad
        self.posy += self.dy_normalizado * self.velocidad

        #Actualizo su rect para que se dibuje en la posicion deseada
        self.rect.x = self.posx
        self.rect.y = self.posy

        # Calculo la nueva distancia al punto de destino
        self.vector_x = self.targetx - self.posx
        self.vector_y = self.targety - self.posy
        self.distancia = math.sqrt(self.vector_x ** 2 + self.vector_y ** 2)