import pygame
from random import randint

pygame.init()

screen = pygame.display.set_mode((500,600))
d = 10
spawn_pipe = pygame.USEREVENT +1
pygame.time.set_timer(spawn_pipe, 700)
pygame.display.set_caption("Doodle Jump")
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)  # allows us to inherit functinallity
        self.image= pygame.image.load("jump2.png")
        self.rect = self.image.get_rect(topleft = (290,50))
        self.gravity = 0
        self.add_gravity = 0.5
        self.d = 0

    def apply_gravity(self):
        self.rect.y+=self.gravity
        self.gravity += self.add_gravity
        if self.rect.bottom>=600:
            self.add_gravity = 0
            self.gravity = 0
            



    def movement(self):
        self.rect.x += self.d
        if self.rect.right<-0:
             self.rect.left=600
        elif self.rect.left>=600:
             self.rect.right=0
        


        

    def collison(self):
        for surf in platform_group:
            if pygame.Rect.colliderect(surf.rect, self.rect):
                if self.rect.bottom<surf.rect.bottom:
                    if self.gravity>0:
                        self.gravity = -14


    def update(self):
        self.apply_gravity()
        self.movement()
        self.collison()

player_group = pygame.sprite.Group()
player = Player()
player_group.add(player)

platform_img = pygame.image.load("Pad_02_1.png")
max_platforms = 15

class Platform(pygame.sprite.Sprite):
    global game_active
    def __init__(self, x, y, width):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(platform_img,(width,15))
        self.rect = self.image.get_rect(center= (x,y))
        self.x = x
        self.y = y
        self.add_gravity = 2.5

    def move(self):
        self.rect.y +=self.add_gravity # makes the platform falls down
        if game_active== None:
            self.add_gravity = 0

    def destroy(self):
        if self.rect.top>=600: # if the platform goes below the screen
            self.kill()



    def update(self):
        self.move()
        self.destroy()

platform_group = pygame.sprite.Group()

for i in range(max_platforms):
    px = randint(20,590)
    py = randint(5,580)
    pwidth = randint(40,60)

    platform = Platform(px, py, pwidth)
    platform_group.add(platform)





spawn_platform = pygame.USEREVENT +1 #create an event
pygame.time.set_timer(spawn_platform, 900)

clock = pygame.time.Clock()
background = pygame.image.load("background0.png")
restart_icon = pygame.image.load("rotate_left-512.png")
restart_button = restart_icon.get_rect(topleft= (100,100))
start_icon = pygame.image.load("sp.png")
start_button = start_icon.get_rect(topleft = (150,50))
pos = pygame.mouse.get_pos()  # get the current mouse pos the entire game so dont put in game_active loop

clicked = False


def start_of_game():
    global clicked,game_active,pos, running
    if game_active == False:
        screen.blit(start_icon,start_button)

        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running=False
                if event.type == pygame.KEYDOWN:
                        if event.key== pygame.K_SPACE:
                            game_active = True
                






game_active = False
running = True
while running:
    screen.blit(background, (0,0))
    start_of_game()
    for event in pygame.event.get():
        if game_active:
            if event.type == pygame.QUIT:
                    running=False
            if event.type == spawn_pipe:
                
                    px = randint(20,590)
                    py = 0
                    pwidth = randint(40,60)

                    platform = Platform(px, py, pwidth)
                    platform_group.add(platform)
            if event.type == pygame.KEYDOWN:
                            if event.key== pygame.K_LEFT:
                                    player.d= -10
                            elif event.key== pygame.K_RIGHT:
                                    player.d= 10
            elif event.type== pygame.KEYUP:
                            player.d = 0
                
    
    if game_active:

        
        platform_group.draw(screen)
        platform_group.update()
        player_group.draw(screen)
        player_group.update()
        
        
        if player.rect.bottom >=600:
            player.rect.y =0
            player.rect.x = 250
            player.add_gravity = 0.5
            for i in range(max_platforms):
                px = randint(20,600)
                py = randint(0,500)
                pwidth = randint(40,60)

                platform = Platform(px, py, pwidth)
                platform_group.add(platform)
            game_active = False
      
            
        
    











    clock.tick(60)
    pygame.display.update()
