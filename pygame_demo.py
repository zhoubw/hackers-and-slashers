import pygame
from pygame.locals import *

#lolololol

window_x = 800
window_y = 600

frames = 0
FPS = 60

pygame.init()

window = pygame.display.set_mode((window_x,window_y),pygame.RESIZABLE)
background = pygame.Surface(window.get_size())
background.fill((0,0,0))
background = background.convert();
window.blit(background,(0,0))

clock = pygame.time.Clock()

running = True


class Player:
    def __init__(self):
        self.pos = [400,300]
        self.radius = 20
        self.speed = 5
    #def __call__(self):
    #    pass
    def movement(self):
        KeyList = pygame.key.get_pressed()
        if KeyList[K_UP]:
            self.pos[1] -= self.speed
        if KeyList[K_DOWN]:
            self.pos[1] += self.speed
        if KeyList[K_LEFT]:
            self.pos[0] -= self.speed
        if KeyList[K_RIGHT]:
            self.pos[0] += self.speed
        pygame.draw.circle(window,(0,0,255),self.pos,self.radius)

player = Player()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    window.fill((0,0,0))

    player.movement()

    clock.tick(FPS)
    frames += 1
    print frames
    #pygame.display.flip()
    pygame.display.update()
pygame.exit()
