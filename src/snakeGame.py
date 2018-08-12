import pygame , sys, random, time

#print(pygame.init());

check_errors = pygame.init();

if check_errors[1]> 0:
    print("(!) had {0} initializing errors, exiting ... ". format(check_errors))
    sys.exit(-1)
else:
    print("(+) PyGame successfully initialized!")

playSurface = pygame.display.set_mode((720,460))
pygame.display.set_caption("snake game")

#colors
red = pygame.Color(255,0,0)
green = pygame.Color(0,255,0)
blue = pygame.Color(0,0,255)
black = pygame.Color(0,0,0)
white = pygame.Color(255,255,255)
brown = pygame.Color(160,42,42)

#loop game
fpsController = pygame.time.Clock()

#snake position
snakePos = [100,50]
snakeBody = [[100,50],[90,50],[80,50]]

foodPos = [random.randrange(1,72)*10, random.randrange(1,46)*10]
foodSpawn = True

direction = 'RIGHT'
changeto = direction

# game over function
def gameOver():
    #set the font from the system
    myFont = pygame.font.SysFont('monaco' , 72)
    GOsurf = myFont.render( 'Game Over' ,  True , red)
    GOrect = GOsurf.get_rect()
    GOrect.midtop = (360 , 15)
    playSurface.blit( GOsurf , GOrect)
    pygame.display.flip()



gameOver()




time.sleep(5)


