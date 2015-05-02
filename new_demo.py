import pygame
from pygame.locals import *
from functions import *

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
powerthing = True

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

#Aesthetics & class code
class Powerup:
    def __init__(self):
        self.pos = [300,300]
        self.width = 50
        self.length = 50
    def appear(self):
        pygame.draw.rect(window,(100,0,100), (300,300,10,10), 5)
	
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

#direction: 1 v = left, 2 = right
direction = 1
class Enemys:
    def __init__(self):
        self.pos = [400,200]
        self.radius = 20
        self.speed = 5
    def movement(self):
        #direction: 1 = left, 2 = right
        if direction == 1:
            self.pos[0] -= self.speed
        if direction == 2:
           self.pos[0] += self.speed
        pygame.draw.circle(window,(50,205,50),self.pos,self.radius)
        

  
wall = wall()
player = Player()
enemy = Enemys()
powerup = Powerup()


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    if player.pos[0] < 90:
        player.pos[0] = 90
    if player.pos[0] > 720:
        player.pos[0] = 720
    if player.pos[1] < 90:
        player.pos[1] = 90
    if player.pos[1] > 520:
        player.pos[1] = 520

    if enemy.pos[0] < 60:
        direction = 2
    if enemy.pos[0] > 740:
        direction = 1
	#This detects if the player moves close to the powerup & then does something
    if (player.pos[0] == powerup.pos[0] - 10 or powerup.pos[0] + 10) & (player.pos[1] == powerup.pos[1] - 10 or powerup.pos[1] + 10):
	powerthing = True
    else:
	#Increase stat & makes powerup dissapear
	powerthing = False
    if powerthing:
	powerup.appear()
        
    window.fill((0,0,0))
    
    wall.draw()
    player.movement()
    enemy.movement()

    clock.tick(FPS)
    frames += 1
    print frames
    #pygame.display.flip()
    pygame.display.update()
pygame.exit()
