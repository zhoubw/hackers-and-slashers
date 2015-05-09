import pygame
import random
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
        self.direction = 2
        # direction, 1=up, 2=right, 3=down, 4=left
        self.timer = 0
        self.limit = 30
        
        self.health = 100
        self.color = [0,0,255]
    def movement(self):
        KeyList = pygame.key.get_pressed()
        if KeyList[K_UP] and self.health > 0:
            self.pos[1] -= self.speed
            self.direction = 3
        if KeyList[K_DOWN] and self.health > 0:
            self.pos[1] += self.speed
            self.direction = 1
        if KeyList[K_LEFT] and self.health > 0:
            self.pos[0] -= self.speed
            self.direction = 4
        if KeyList[K_RIGHT] and self.health > 0:
            self.pos[0] += self.speed
            self.direction = 2
        self.timer += 1
        pygame.draw.circle(window,(self.color),self.pos,self.radius)

# projdir (projectile-direction)
# projdir, 1=up, 2=right, 3=down, 4=left
# projmode (projectile-mode)
# projmode 1=shot, outside of player, 2=in player (being held onto)

class Projectiles:
    def __init__(self):
        self.pos = [400,300]
        self.radius = 5
        self.speed = 0
        self.projdir = 2
        self.projmode = 2
        self.pos = player.pos
        self.timer = 0
        self.limit = 30
    def movement(self):
        KeyList = pygame.key.get_pressed()
        self.direction = player.direction
        self.timer += 1
        if KeyList[K_SPACE] and self.projmode == 1 and self.timer > self.limit:
            self.pos = player.pos
            self.speed = 0
            self.projmode = 2
            self.timer = 0
        elif KeyList[K_SPACE] and self.projmode == 2 and self.timer > self.limit:
            self.pos = [player.pos[0], player.pos[1]]
            self.speed = 2
            self.projmode = 1
            self.timer = 0

        if self.direction == 1:
            self.pos[1] += self.speed
        if self.direction == 2:
           self.pos[0] += self.speed
        if self.direction == 3:
            self.pos[1] -= self.speed
        if self.direction == 4:
           self.pos[0] -= self.speed
        
        pygame.draw.circle(window,(200,200,200),self.pos,self.radius)
        


class Enemys:
    def __init__(self, position):
        self.pos = position
        self.radius = 20
        self.speed = 5
        self.direction = 1
        self.health = 40
    def movement(self):
        #direction: 1 = left, 2 = right
        if self.direction == 1:
            self.pos[0] -= self.speed
        if self.direction == 2:
            self.pos[0] += self.speed
        pygame.draw.circle(window,(50,205,50),self.pos,self.radius)

        if self.pos[0] < 60:
            self.direction = 2
        if self.pos[0] > 740:
            self.direction = 1
        

  
wall = wall()
player = Player()
projectile = Projectiles()
powerup = Powerup()

numEnemys = 5 # total number of enemies
badguyArray = []
for index in xrange(numEnemys):
    badguyArray.append(Enemys([(100), (index * 100 + 100)]))

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
        
    for i in badguyArray:
        if abs(player.pos[0] - i.pos[0]) <= 20 and abs(player.pos[1] - i.pos[1]) <= 20 and player.timer > player.limit:
            player.health -= 10
            print(player.health)
            player.timer = 0
    if player.health <= 0:
        player.color = (255,0,0)
        print("You died!!")
            
    for eachEnemy in badguyArray:
        if abs(projectile.pos[0] - eachEnemy.pos[0]) <= 40 and abs(projectile.pos[1] - eachEnemy.pos[1]) <= 40:
            eachEnemy.health -= 20
    for eachEnemy in badguyArray:
        if eachEnemy.health <= 0:
            badguyArray.remove(eachEnemy)
            #print("Badguy #" + str(eachEnemy) + "is down!!")


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
    projectile.movement()
    
    for eachEnemy in badguyArray:
        eachEnemy.movement()

    clock.tick(FPS)
    frames += 1
    #print frames
    #pygame.display.flip()
    pygame.display.update()
pygame.quit()
