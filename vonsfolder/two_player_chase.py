import pygame
from pygame.locals import *

#this is von's chase game and it is awesome

window_x = 1200
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


class Player3:
    #rose brown
    def __init__(self):
        self.pos = [1000,200]
        self.radius = 35
        self.speed = 5
    def movement(self):
        KeyList = pygame.key.get_pressed()
        if KeyList[K_t]:
            self.pos[1] -= self.speed
        if KeyList[K_g]:
            self.pos[1] += self.speed
        if KeyList[K_f]:
            self.pos[0] -= self.speed
        if KeyList[K_h]:
            self.pos[0] += self.speed
        pygame.draw.circle(window,(188,143,143),self.pos,self.radius)

player3 = Player3()
class Player2:
    #the good guy
    def __init__(self):
        self.pos = [200,200]
        self.radius = 35
        self.speed = 5
    def movement(self):
        KeyList = pygame.key.get_pressed()
        if KeyList[K_w]:
            self.pos[1] -= self.speed
        if KeyList[K_s]:
            self.pos[1] += self.speed
        if KeyList[K_a]:
            self.pos[0] -= self.speed
        if KeyList[K_d]:
            self.pos[0] += self.speed
        pygame.draw.circle(window,(200,0,255),self.pos,self.radius)

player2 = Player2()
class Player:
    #purple circle
    def __init__(self):
        self.pos = [600,400]
        self.radius = 20
        self.speed = 8
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
        pygame.draw.circle(window,(10,255,120),self.pos,self.radius)

player = Player()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    if player.pos[0] < 5:
        player.pos[0] = 1190
    if player.pos[0] > 1195:
        player.pos[0] = 10
    if player.pos[1] < 5:
        player.pos[1] = 590
    if player.pos[1] > 595:
        player.pos[1] = 10
    if player2.pos[0] < 5:
        player2.pos[0] = 1190
    if player2.pos[0] > 1195:
        player2.pos[0] = 10
    if player2.pos[1] < 5:
        player2.pos[1] = 590
    if player2.pos[1] > 595:
        player2.pos[1] = 10
    if player3.pos[0] < 5:
        player3.pos[0] = 1190
    if player3.pos[0] > 1195:
        player3.pos[0] = 10
    if player3.pos[1] < 5:
        player3.pos[1] = 590
    if player3.pos[1] > 595:
        player3.pos[1] = 10
    window.fill((0,0,0))

    player3.movement()
    player2.movement()
    player.movement()

    clock.tick(FPS)
    frames += 1
    print frames
    #pygame.display.flip()
    pygame.display.update()
pygame.exit()
