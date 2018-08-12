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
    time.sleep(5)
    pygame.quit()
    sys.exit()

#logic loop of game
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(-1)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                changeto = 'RIGHT'
            elif event.key == pygame.K_LEFT or event.key == ord('a'):
                changeto = 'LEFT'
            elif event.key == pygame.K_UP or event.key == ord('w'):
                changeto = 'UP'
            elif event.key == pygame.K_DOWN or event.key == ord('s'):
                changeto = 'DOWN'
            elif event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))

    #validation direction
    if changeto == 'RIGHT' and not direction == 'LEFT':
        direction =='RIGHT'
        #validation direction
    if changeto == 'LEFT' and not direction == 'RIGHT':
        direction =='LEFT'
        #validation direction
    if changeto == 'UP' and not direction == 'DOWN':
        direction =='UP'
        #validation direction
    if changeto == 'DOWN' and not direction == 'UP':
        direction =='DOWN'

    if direction == 'RIGHT':
        snakePos[0] += 10
    if direction == 'LEFT':
        snakePos[0] -= 10
    if direction == 'UP':
        snakePos[1] -= 10
    if direction == 'DOWN':
        snakePos[1] += 10

    #body mechanism
    snakeBody.insert(0, list(snakePos))
    if snakePos[0] == foodPos[0] and snakePos[1] ==foodPos[1]:
        foodSpawn = False
    else:
        snakeBody.pop()

    if foodSpawn == False:
        foodPos = [random.randrange(1,72)*10, random.randrange(1,46)*10]

    foodSpawn = True













