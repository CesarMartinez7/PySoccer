import pygame.font


class ButtonPlay(pygame.sprite.Sprite):
    def __init__(self,):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load("./assets/play.png")
        self.react=self.image.get_rect()
    
        
    def draw(self,ventana) -> None:
        self.ventanaSurface=ventana
        self.ventanaSurface.blit(self.image,self.react)
        