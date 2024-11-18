from ursina import *


game=Ursina()


class Cubo(Entity):
    def __init__(self,color=color.white50,scale=(1,1,1),position=(0,-3,0)):
        super().__init__()
        self.color=color
        self.scale=scale
        self.model="circle"
        self.position=position
        self.gravity=1
        self.salto=False
        self.velocidad_salto=40
        print(scale)
    
    def mover(self):
        if held_keys["w"] or held_keys["up arrow"]:
            self.y+=1 * time.dt
        if held_keys["s"] or held_keys["down arrow"]:
            self.y-=1 * time.dt
        if held_keys["d"] or held_keys["right arrow"]:
            self.x +=1 * time.dt
        if held_keys["a"] or held_keys["left arrow"]:
            self.x -=1 * time.dt
#LE PEDI AYUDA A CLAUDE PERO
    def limite_pantalla(self):
        self.x = max(-1, min(self.x, 1))  # Cambia -10 y 10 según los límites deseados
        self.y = max(0, min(self.y, 10))

    def saltar(self):
        if held_keys["space"] and not self.salto:
            self.salto = True
            self.y += self.velocidad_salto * time.dt
            if self.salto:
                self.y-=self.gravity*time.dt
        elif self.salto:
            self.y -= self.gravity * time.dt
            if self.y <= 0:  # Regresar al suelo
                self.y = 0
                self.salto = False
    def update(self):
        cubo1.mover()
        cubo1.saltar()
cubo1=Cubo()
    

game.run()


