import pygame

from resources.Colors import WHITE


class Jugador:
    """Clase jugador, para el jugador principal de la partida,
    metodos para dibujar y interactuar con el objeto jugador en la clase JuegoPrincipal"""

    def __init__(self, imagen, ancho, alto, salud,velocidad,danio):
        self.imagen = pygame.image.load(imagen)  # Cargar la imagen de la nave
        self.ancho=100   # Ancho deseado para la nave
        self.alto=100    # Alto
        self.imagen = pygame.transform.scale(self.imagen, (self.ancho, self.alto))  # Redimensionar la imagen

        self.rect = self.imagen.get_rect(center=(ancho // 2, alto - 50))  # Obtener el rectángulo de la nave y centrarla

        #Variables del jugador
        self.salud = salud          #Vida o salud actual del jugador (Durante la partida)
        self.velocidad=velocidad        #Velocidad a la que se desplaza al moverse
        self.puntos=0               #Puntos obtenidos en la partida
        self.danio=danio                #Daño contra enemigos
        self.saludInicial=salud     #Salud con la que inicia la partida, para pintar la barra de vida


    def sumarPuntos(self,puntos):
        self.puntos+=puntos #Para cuando el jugador derrota a un enemigo

    def dibujar(self, superficie,ancho,alto):
        """Metodo que dibuja todos los elementos de la pantalla asociados al jugador (Salvo balas)"""
        superficie.blit(self.imagen, self.rect)  # Dibujar la imagen de la nave del jugador
        self.dibujar_barra_vida(superficie,ancho,alto)  # Dibujar la barra de vida
        self.dibujar_puntuacion(superficie,ancho,alto)  # Dibujar puntuacion actual


    def dibujar_puntuacion(self,superficie,ancho,alto):
        """Metodo para dibujar la puntuacion del jugador en tiempo real"""
        WHITE = (255, 255, 255)  # Color blanco
        font = pygame.font.Font(None, 40) #Fuente y tamaño
        textoMostrar = font.render("Puntuacion: "+str(self.puntos), True, WHITE) #Texto final
        superficie.blit(textoMostrar, (ancho-300,20)) #Dinujar texto

    def dibujar_barra_vida(self, superficie,ancho,alto):
        RED = (255, 0, 0)
        GREEN=(0,255,0)
        # Barra de vida
        vida_ancho = 20  # Ancho de la barra de vida
        vida_alto = 200    # Alto de la barra de vida
        porcentaje_vida = self.salud / self.saludInicial #Porcentaje de vida actual
        pygame.draw.rect(superficie, RED, (ancho-25, alto-220, vida_ancho, vida_alto))  # Fondo rojo que se ve al perder vida
        pygame.draw.rect(superficie, GREEN, (ancho-25, alto-220, vida_ancho, vida_alto* porcentaje_vida))  # Vida actual en verde

    def recibir_dano(self, dano):
        """Metodo para cuando el jugador recive una bala enemiga"""
        self.salud -= dano
        if self.salud < 0:
            self.salud = 0  # No permitir que la salud sea negativa

    def moverIzquierda(self):
        """Movimiento a la izqda"""
        self.rect.x -= self.velocidad  # Mover la nave a la izquierda

    def moverDerecha(self):
        """Movimiento a la drcha"""
        self.rect.x += self.velocidad  # Mover la nave a la derecha