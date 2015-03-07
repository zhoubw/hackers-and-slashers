import pygame
from pygame.locals import *

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

class wall:
    def __init__(self):
        self.pos = [100,300]
        self.width = 100
        self.length = 200
    def draw(self):
        #pygame.draw.rect(screen, color, (x,y,width,height), thickness)
        pygame.draw.rect(window,(255,0,0), (50,50,10,500), 10) # left wall - down
        pygame.draw.rect(window, (255,0,0), (750,50,-700,10), 10) # up wall - left
        pygame.draw.rect(window,(255,0,0), (750,550,10,-500), 10) # right wall - up
        pygame.draw.rect(window, (255,0,0), (50,550,700,10), 10) # down wall - right
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
wall = wall()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    if player.pos[0] < 60:
        player.pos[0] = 70
    if player.pos[0] > 740:
        player.pos[0] = 730
    if player.pos[1] < 60:
        player.pos[1] = 70
    if player.pos[1] > 540:
        player.pos[1] = 530
    window.fill((0,0,0))

    player.movement()
    wall.draw()

    clock.tick(FPS)
    frames += 1
    print frames
    #pygame.display.flip()
    pygame.display.update()
pygame.exit()
