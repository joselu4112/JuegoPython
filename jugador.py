import pygame

from resources.Colors import WHITE


class Jugador:
    def __init__(self, imagen, ancho, alto, salud,velocidad,danio):
        self.imagen = pygame.image.load(imagen)  # Cargar la imagen de la nave
        self.ancho=100  # Ancho deseado para la nave
        self.alto=100    # Alto
        self.imagen = pygame.transform.scale(self.imagen, (self.ancho, self.alto))  # Redimensionar la imagen

        self.rect = self.imagen.get_rect(center=(ancho // 2, alto - 50))  # Obtener el rectángulo de la nave y centrarla

        self.salud = salud
        self.velocidad=velocidad
        self.puntos=0
        self.danio=danio
        self.saludInicial=salud


    def sumarPuntos(self,puntos):
        self.puntos+=puntos

    def dibujar(self, superficie,ancho,alto):
            superficie.blit(self.imagen, self.rect)  # Dibujar la imagen del enemigo
            self.dibujar_barra_vida(superficie,ancho,alto)  # Dibujar la barra de vida
            self.dibujar_puntuacion(superficie,ancho,alto)


    def dibujar_puntuacion(self,superficie,ancho,alto):
        WHITE = (255, 255, 255)  # Color blanco en formato RGB
        font = pygame.font.Font(None, 40)
        textoMostrar = font.render("Puntuacion: "+str(self.puntos), True, WHITE)
        superficie.blit(textoMostrar, (ancho-300,20))

    def dibujar_barra_vida(self, superficie,ancho,alto):
        RED = (255, 0, 0)
        GREEN=(0,255,0)
        # Barra de vida
        vida_ancho = 20  # Ancho de la barra de vida
        vida_alto = 200    # Alto de la barra de vida
        porcentaje_vida = self.salud / self.saludInicial
        pygame.draw.rect(superficie, RED, (ancho-25, alto-220, vida_ancho, vida_alto))  # Fondo
        pygame.draw.rect(superficie, GREEN, (ancho-25, alto-220, vida_ancho, vida_alto* porcentaje_vida))  # Vida actual

    def recibir_dano(self, dano):
        self.salud -= dano
        if self.salud < 0:
            self.salud = 0  # No permitir que la salud sea negativa

    def moverIzquierda(self):
        self.rect.x -= self.velocidad  # Mover la nave a la izquierda

    def moverDerecha(self):
        self.rect.x += self.velocidad  # Mover la nave a la derecha