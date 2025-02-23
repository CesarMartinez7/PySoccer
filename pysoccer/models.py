import pygame
from typing import Any


#  Clase balon que tiene movimiento optimizado


RESOLUCION : tuple = (780, 980)

class Balon(pygame.sprite.Sprite):
    def __init__(self, velocidad: list[int]) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("./assets/SoccerBall.png")
        self.react = self.image.get_rect()
        self.move_ip = self.react.move_ip(440, 50)
        self.velocidad = velocidad
        self.movimiento = self.react.move(velocidad)

    # La actualizacion que hace que el balon se mueva
    def actualizar(self) -> None:
        self.react = self.react.move(self.velocidad)

    def draw(self, ventanaGame) -> None:
        self.ventanaSurface = ventanaGame
        self.ventanaSurface.blit(self.image, self.react)


# Clase con atributos del Kate


class Kate(pygame.sprite.Sprite):
    def __init__(self) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.images = {
            "kateLeftTop": pygame.image.load("./assets/player1/left_top.png"),
            "kateRightBottom": pygame.image.load("./assets/player1/right_bottom.png"),
            "kateLeft": pygame.image.load(
                "./assets/player1/left.png"
            ),  
            "kateRight": pygame.image.load(
                "./assets/player1/right.png"
            ),  
            "kateDefault": pygame.image.load(
                "./assets/player1/default.png"
            ),  
            "kateBack": pygame.image.load("./assets/player1/back.png"),
        }

        self.rect = self.images["kateDefault"].get_rect()
        self.rect.move_ip(400, 800)
        self.imagenActual = self.images["kateDefault"]

    def draw(self, ventanaGame) -> None:
        self.ventanaSurface = ventanaGame
        self.ventanaSurface.blit(self.imagenActual, self.rect)

    def movimientos(self) -> None:
        self.botones = pygame.key.get_pressed()
        if self.botones[pygame.K_LEFT]:
            self.rect = self.rect.move(-3, 0)
            self.imagenActual = self.images["kateLeft"]
        if self.botones[pygame.K_RIGHT]:
            self.rect = self.rect.move(3, 0)
            self.imagenActual = self.images["kateRight"]
        if self.botones[pygame.K_UP]:
            self.rect = self.rect.move(0, -3)
            self.imagenActual = self.images["kateDefault"]
        if self.botones[pygame.K_DOWN]:
            self.rect = self.rect.move(0, 3)
            self.imagenActual = self.images["kateBack"]
        if self.botones[pygame.K_UP] and self.botones[pygame.K_LEFT]:
            self.imagenActual = self.images["kateLeftTop"]
        if self.botones[pygame.K_DOWN] and self.botones[pygame.K_RIGHT]:
            self.imagenActual = self.images["kateRightBottom"]
            print("Aqui")


# Clase con atributos de Messi


class Messi(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images = {
            "lidiaRight": pygame.image.load("./assets/player2/right.png"),
            "lidiaDefault": pygame.image.load("./assets/player2/default.png"),
            "lidiaLeft": pygame.image.load("./assets/player2/left.png"),
            "lidiaBack": pygame.image.load("./assets/player2/back.png"),
        }
        self.image = self.images["lidiaDefault"]
        self.rect = self.image.get_rect()
        self.rect.move_ip(400, 1)
        self.run = False

    def movimientos(self) -> None:
        self.botones = pygame.key.get_pressed()
        if self.botones[pygame.K_a]:
            self.rect = self.rect.move(-3, 0)
            self.run = True
            self.image = self.images["lidiaLeft"]
        if self.botones[pygame.K_d]:
            self.rect = self.rect.move(3, 0)
            self.run = True
            self.image = self.images["lidiaRight"]
        if self.botones[pygame.K_w]:
            self.run = True
            self.rect = self.rect.move(0, -3)
            self.image = self.images["lidiaDefault"]
        if self.botones[pygame.K_s]:
            self.rect = self.rect.move(0, 3)
            self.run = True
            self.image = self.images["lidiaBack"]

    def draw(self, ventanaGame) -> None:
        self.ventanaSurface = ventanaGame
        self.ventanaSurface.blit(self.image, self.rect)


class SinglentonMetaMusic(type):
    _instancia = dict()

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instancia:
            instancia = super().__call__(*args, **kwargs)
            cls._instancia[cls] = instancia
        return cls._instancia[cls]


# Clase para la musica de de fondo o para otras cosas
class Musica(metaclass=SinglentonMetaMusic):
    def __init__(self, cancion) -> None:
        self.cancion = cancion
        pygame.mixer.init()
        pygame.mixer.music.load(cancion)
        self.reproducir()

    def reproducir(self) -> None:
        pygame.mixer.music.play(-1)


# Sonidos class (PRINCIPALMENTE PARA COLLISIONES O DISPAROS)


class Sonidos:
    def __init__(self):
        pygame.mixer.init()

    def reproducir(self, sound):
        self.sonido = pygame.mixer.Sound(sound)
        self.sonido.play()


# PROXIMAMENTE AÑADIR COLLISION CON LA VENTANA PARA Q EL PERSONAJE NO PASE DE LA VENTANA
