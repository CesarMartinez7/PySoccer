import pygame
from typing import Any


#  Clase balon que tiene movimiento optimizado 

class Balon(pygame.sprite.Sprite):
    def __init__(self, velocidad: list[int]) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load("./assets/SoccerBall.png")
        self.react=self.image.get_rect()
        self.move_ip=self.react.move_ip(0,0)
        self.velocidad=velocidad
        self.movimiento=self.react.move(velocidad)
        

    #La actualizacion que hace que el balon se mueva
    def actualizar(self) -> None:
        self.react = self.react.move(self.velocidad)  
    
    def draw(self,ventanaGame) -> None:
        self.ventanaSurface=ventanaGame
        self.ventanaSurface.blit(self.image,self.react)


# Clase con atributos del FANTASMA

class Ghost(pygame.sprite.Sprite):
    def __init__(self) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.images={
            "ghostLEFT":pygame.image.load("./assets/ghost_left.png"), #Imagen de la izquierda
            "ghostRIGHT":pygame.image.load("./assets/ghost_RIGHT.png"), # Imagen de la derecha
            "ghostDefault":pygame.image.load("./assets/ghost_RIGHT.png") # Imagen default
        }
        self.rect=self.images["ghostDefault"].get_rect()
        self.rect.move_ip(400,800)
        self.imagenActual=self.images["ghostDefault"]
        
    def draw(self,ventanaGame) -> None:
        self.ventanaSurface=ventanaGame
        self.ventanaSurface.blit(self.imagenActual,self.rect)
    
    def movimientos(self) -> None:
        self.botones=pygame.key.get_pressed()
        if self.botones[pygame.K_LEFT]:
            self.rect=self.rect.move(-3,0)
            self.imagenActual=self.images["ghostLEFT"]
        if self.botones[pygame.K_RIGHT]:
            self.rect=self.rect.move(3,0)
            self.imagenActual=self.images["ghostRIGHT"]
        if self.botones[pygame.K_UP]:
            self.rect=self.rect.move(0,-3)
        if self.botones[pygame.K_DOWN]:
            self.rect=self.rect.move(0,3)
    


# Clase con atributos de Messi

class Messi(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("./assets/playerDefault.png")
        self.rect = self.image.get_rect()
        self.rect.move_ip(400,1)
        self.run=False

        
    def movimientos(self) -> None:
        self.botones =pygame.key.get_pressed()
        if self.botones[pygame.K_a]:  
            self.rect = self.rect.move(-3, 0)
            self.run=True
        if self.botones[pygame.K_d]:
            self.rect=self.rect.move(3,0)
            self.run=True
        if self.botones[pygame.K_w]:
            self.run=True
            self.rect=self.rect.move(0,-3)
        if self.botones[pygame.K_s]:
            self.rect=self.rect.move(0,3)
            self.run=True
            
                
    def draw(self,ventanaGame) -> None:
        self.ventanaSurface=ventanaGame
        self.ventanaSurface.blit(self.image,self.rect)

class SinglentonMetaMusic(type):
    _instancia=dict()
    def __call__(cls,*args, **kwargs):
        if cls not in cls._instancia:
            instancia=super().__call__(*args, **kwargs)
            cls._instancia[cls] = instancia
        return cls._instancia[cls]



# Clase para la musica de de fondo o para otras cosas
class Musica(metaclass=SinglentonMetaMusic):
    def __init__(self,cancion) -> None:
        self.cancion=cancion
        pygame.mixer.init() 
        pygame.mixer.music.load(cancion)  
        self.reproducir()
        
    def reproducir(self) -> None:
        pygame.mixer.music.play(-1) 
        

# Sonidos class (PRINCIPALMENTE PARA COLLISIONES O DISPAROS)

class Sonidos():
    def __init__(self):
        pygame.mixer.init()

    def reproducir(self,sound):
        self.sonido=pygame.mixer.Sound(sound)
        self.sonido.play()
        


# PROXIMAMENTE AÑADIR COLLISION CON LA VENTANA PARA Q EL PERSONAJE NO PASE DE LA VENTANA