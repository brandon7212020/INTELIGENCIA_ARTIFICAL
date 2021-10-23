import pygame
import random
ANCHO=1200
ALTO=900
rojo=[255,0,0]
blanco=[255,255,255]
azul=[0,255,255]
verde=[54,228,11]
morado=[116,11,228]
negro=[0,0,0]
amarillo=[255,255,0]
class Jugador(pygame.sprite.Sprite):
    def __init__(self,pos):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface([60,60])
        self.image.fill(verde)
        self.rect=self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]
        self.velx=0
        self.vely=0

    def update(self):
        if self.rect.y <= 0:
            self.vely=5
        if self.rect.x <= 0:
            self.velx=5
        if self.rect.y >= 650:
            self.vely=-5
        if self.rect.x >= 1150:
            self.velx=-5
        self.rect.x+=self.velx
        self.rect.y+=self.vely

class Rival(pygame.sprite.Sprite):
    def __init__(self,pos):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface([60,60])
        self.image.fill(rojo)
        self.rect=self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]
        self.velx=0
        self.vely=0

    def update(self):
        self.rect.x+=self.velx
        self.rect.y+=self.vely


if __name__ == '__main__':
    import pygame
    ventana=pygame.display.set_mode([ANCHO,ALTO])
    jugadores=pygame.sprite.Group()
    rivales=pygame.sprite.Group()
    j=Jugador([200,100])
    jugadores.add(j)

    n=30

    for i in range(n):
        x=random.randrange(0,ANCHO-60)
        y=random.randrange(0,ALTO-60)
        r=Rival([x,y])
        rivales.add(r)

    reloj=pygame.time.Clock()
    fin=False
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    j.velx=5
                    j.vely=0
                if event.key == pygame.K_LEFT:
                    j.velx=-5
                    j.vely=0
                if event.key == pygame.K_DOWN:
                    j.velx=0
                    j.vely=5
                if event.key == pygame.K_UP:
                    j.velx=0
                    j.vely=-5

        for r in rivales:
            lsm=pygame.sprite.spritecollide(r,jugadores,False)
            for j in lsm:
                d=random.randrange(0,10)
                f=0

                if j.velx!=0:
                    if d < 5:
                        j.vely=5
                    else:
                        j.vely=-5
                    j.rect.x=j.rect.x-j.velx
                    j.velx=0
                    f=1

                if f == 0:
                    if j.vely!=0:
                        if d < 5:
                            j.velx=5
                        else:
                            j.velx=-5
                        j.rect.y=j.rect.y-j.vely
                        j.vely=0


        jugadores.update()
        rivales.update()
        ventana.fill(negro)
        jugadores.draw(ventana)
        rivales.draw(ventana)
        pygame.display.flip()
        reloj.tick(40)
