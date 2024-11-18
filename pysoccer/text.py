import pygame
import sys

# Inicializar Pygame
pygame.init()

pantalla=pygame.display.set_mode((200,200))



jugando=True

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jugando=False
            sys.exit()
    
    
    fuente = pygame.font.SysFont("Console",60)
    mensaje="fOOTBALLL MANAGER"
    render=fuente.render(mensaje,True,(20,20,20))
    
    pantalla.blit(render,(10,10))
    pygame.display.flip()