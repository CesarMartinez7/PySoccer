import pygame
from models import (Balon,Ghost,Musica,Sonidos,Messi)
pygame.init()

FONDOVENTANA=pygame.image.load("./assets/football-pitch.png")

colores=(0,0,0)
RESOLUCION=(780,980)

ventana=pygame.display.set_mode(RESOLUCION)

pygame.display.set_caption("PySoccer")

ICON=pygame.image.load("./assets/SoccerBall.png")
pygame.display.set_icon(ICON)


musica = Musica("./sounds/aiport.mp3")

collision_balon=Sonidos()


velocidad=[6,6]    


#Instancias Objetos de Display
player1=Ghost()
player2=Messi()
balon=Balon(velocidad=velocidad)


ESTADO_JUGANDO=True
# Collisiones de los personajes y pelotas
def Collisiones():        
    if player1.rect.colliderect(balon.react):
        balon.velocidad[1]= -balon.velocidad[1]
        collision_balon.reproducir("./sounds/8.ogg")
        print(puntos)
    if player2.rect.colliderect(balon.react):
        balon.velocidad[1]= - balon.velocidad[1]
        collision_balon.reproducir("./sounds/8.ogg")
# Movimientos de los personajes       
def movimientosPersonajes():
    player2.movimientos()
    player1.movimientos()



puntos=0


while ESTADO_JUGANDO:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            ESTADO_JUGANDO=False
    
    movimientosPersonajes()
    Collisiones()
    balon.actualizar()
    if balon.react.left < 0 or balon.react.right > ventana.get_width():
        balon.velocidad[0]=-balon.velocidad[0]
    if balon.react.top < 0 or balon.react.bottom > ventana.get_height():
        balon.velocidad[1] = -balon.velocidad[1]
        
    # if player1.rect.left < 0 or player1.rect.right > ventana.get_height():
    #     print("pegado izquierda")
    #     player1.rect.move(y=0) = -player1.rect.move(y=0)
    
    # if player1.rect.left < 0 or player1.rect.right > ventana.get_width():
    #     print("pegado izquierda")
    #     player1.rect.move[0] = -player1.rect.move[0]  # Invertir la velocidad horizontal
    ventana.fill(color=colores)
    ventana.blit(FONDOVENTANA,(0,2))
    
    balon.draw(ventanaGame=ventana)
    player1.draw(ventanaGame=ventana)
    player2.draw(ventanaGame=ventana)

    
    
    pygame.display.flip()
    pygame.time.Clock().tick(90)

pygame.quit()    
