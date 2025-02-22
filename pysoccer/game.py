import pygame
from models import Balon, Kate, Musica, Sonidos, Messi

pygame.init()

FONDOVENTANA = pygame.image.load("./assets/football-pitch.png")

colores = (0, 0, 0)
RESOLUCION = (780, 980)

ventana = pygame.display.set_mode(RESOLUCION)

pygame.display.set_caption("PySoccer")

ICON = pygame.image.load("./assets/SoccerBall.png")
pygame.display.set_icon(ICON)


musica = Musica("./sounds/aiport.mp3")

collision_balon = Sonidos()


velocidad: list = [6, 6]


# Instancias Objetos de Display
player1: object = Kate()
player2: object = Messi()
balon = Balon(velocidad=velocidad)
puntos = 0

ESTADO_JUGANDO: bool = True


# Collisiones de los personajes y pelotas
def Collisiones():
    if player1.rect.colliderect(balon.react):
        balon.velocidad[1] = -balon.velocidad[1]
        collision_balon.reproducir("./sounds/8.ogg")
    if player2.rect.colliderect(balon.react):
        balon.velocidad[1] = -balon.velocidad[1]
        collision_balon.reproducir("./sounds/8.ogg")


# Movimientos de los personajes
def movimientosPersonajes():
    player2.movimientos()
    player1.movimientos()


goles_kate: int = 0
goles_messi: int = 0


while ESTADO_JUGANDO:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ESTADO_JUGANDO = False

    movimientosPersonajes()
    Collisiones()
    balon.actualizar()
    if balon.react.left < 0 or balon.react.right > ventana.get_width():
        balon.velocidad[0] = -balon.velocidad[0]
    if balon.react.top < 0 or balon.react.bottom > ventana.get_height():
        print(ventana.get_height() / 2)
        if ventana.get_height() / 2 and balon.react.bottom:
            goles_kate += 1
            print(f"Gol de Kate {goles_kate}")
        if ventana.get_height() / 2 and balon.react.top:
            goles_messi += 1
            print(f"Gold de Messi {goles_messi}")   
        balon.velocidad[1] = -balon.velocidad[1]
    boton = pygame.key.get_pressed() 
    if boton[pygame.K_ESCAPE]:
        ESTADO_JUGANDO = False

    if balon.react.right == 234:
        ESTADO_JUGANDO = False

    ventana.fill(color=colores)
    ventana.blit(FONDOVENTANA, (0, 2))

    balon.draw(ventanaGame=ventana)
    player1.draw(ventanaGame=ventana)
    player2.draw(ventanaGame=ventana)

    pygame.display.flip()
    pygame.time.Clock().tick(90)

pygame.quit()
