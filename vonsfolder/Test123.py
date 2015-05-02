import pygame
from pygame.locals import *
from functions_von import *

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

class Base(object):
    def __init__(self):
        self.health = 100
        self.pos = pos = [400,300]
        self.radius = 20
        self.speed = 5
        self.direction = 2

    def draw(self):
        pygame.draw.circle(window,(0,0,255),self.pos,self.radius)

class Player(Base):
    def __init__(self):
        super(Player, self).__init__()
        self.pos = pos = [400, 200]

    def movement(self):
        KeyList = pygame.key.get_pressed()
        if KeyList[K_UP]:
            self.pos[1] -= self.speed
            self.direction = 3
        if KeyList[K_DOWN]:
            self.pos[1] += self.speed
            self.direction = 1
        if KeyList[K_LEFT]:
            self.pos[0] -= self.speed
            self.direction = 4
        if KeyList[K_RIGHT]:
            self.pos[0] += self.speed
            self.direction = 2

class Enemy(Base):
    def __init__(self):
        super(Enemy, self).__init__()
        self.pos = pos = [400,100]

    def draw(self):
        pygame.draw.circle(window,(0,255,0),self.pos,self.radius)

    def movement(self):
        #direction: 1 = left, 2 = right
        if self.direction == 1:
            self.pos[0] -= self.speed
        if self.direction == 2:
           self.pos[0] += self.speed

player = Player()
print player.health

"""

class Player:
    def __init__(self):
        self.pos = [400,300]
        self.radius = 20
        self.speed = 5
        self.direction = 2
        # direction, 1=up, 2=right, 3=down, 4=left
    #def __call__(self):
    #    pass

    def movement(self):
        KeyList = pygame.key.get_pressed()
        if KeyList[K_UP]:
            self.pos[1] -= self.speed
            self.direction = 3
        if KeyList[K_DOWN]:
            self.pos[1] += self.speed
            self.direction = 1
        if KeyList[K_LEFT]:
            self.pos[0] -= self.speed
            self.direction = 4
        if KeyList[K_RIGHT]:
            self.pos[0] += self.speed
            self.direction = 2

    def draw(self):
        pygame.draw.circle(window,(0,0,255),self.pos,self.radius)

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

# projdir (projectile-direction)
# projdir, 1=up, 2=right, 3=down, 4=left
# projmode (projectile-mode)
# projmode 1=shot, outside of player, 2=in player (being held onto)

class Projectiles:
    def __init__(self):
        self.pos = [400,300]
        self.radius = 5
        self.speed = 2
        self.projdir = 2
        self.projmode = 1
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

    def draw(self):
        pygame.draw.circle(window,(200,200,200),self.pos,self.radius)

class Enemys:
    def __init__(self):
        self.pos = [400,200]
        self.radius = 20
        self.speed = 5
        self.direction = 1
    def movement(self):
        #direction: 1 = left, 2 = right
        if self.direction == 1:
            self.pos[0] -= self.speed
        if self.direction == 2:
           self.pos[0] += self.speed

    def draw(self):
        pygame.draw.circle(window,(50,205,50),self.pos,self.radius)
"""

#wall = wall()
player = Player()
#projectile = Projectiles()
enemy = Enemy()


#movement
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    #movement of player  
    if player.pos[0] < 60:
        player.pos[0] = 70
    if player.pos[0] > 740:
        player.pos[0] = 730
    if player.pos[1] < 60:
        player.pos[1] = 70
    if player.pos[1] > 540:
        player.pos[1] = 530

    #movement of enemy
    if enemy.pos[0] < 60:
        enemy.direction = 2
    if enemy.pos[0] > 740:
        enemy.direction = 1
        
    window.fill((0,0,0))

    #calls draw functions
    player.draw()
    #wall.draw()
    enemy.draw()
    #projectile.draw()
    #calls move funcitons
    player.movement()
    #projectile.movement()
    enemy.movement()

    clock.tick(FPS)
    frames += 1
    print frames
    #pygame.display.flip()
    pygame.display.update()

#pygame.exit()
