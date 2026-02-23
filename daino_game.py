import pygame
import time

pygame.init()

screen = pygame.display.set_mode((800,600))
font = pygame.font.Font(None, 36)
big_font = pygame.font.Font(None, 74)

pygame.display.set_caption('Dinogame')
icon = pygame.image.load('daino.png')
pygame.display.set_icon(icon)

player_img = pygame.image.load('daino.png')
playerX=1
playerY=300
playerY_ground=300

enemy_img = pygame.image.load('enemy.png')
enemyX=800
enemyY=300

enemy2_img = pygame.image.load('enemy2.png')
enemy2X=400
enemy2Y=300


clock = pygame.time.Clock()
FPS = 60


font = pygame.font.Font('freesansbold.ttf',34)
textX=340
textY=10

over_font = pygame.font.Font("freesansbold.ttf",32)

def show_score(x,y,score):
    rounded_score = round(score)
    score = font.render("score :" + str(rounded_score),True,(255,255,255))
    screen.blit(score, (x,y))

def game_over():
    over_text = over_font.render("GAME OVER" ,True,(255,255,255))
    screen.blit(over_text, (300,230))

start=time.time()
def show_time(seconds):
    minutes = int(seconds // 60)
    seconds = int(seconds % 60)
    return f"{minutes:02d}:{seconds:02d}"

def player(x,y):
    screen.blit(player_img, (x,y))

def enemy(x,y):
    screen.blit(enemy_img, (x,y))

def enemy2(x,y):
    screen.blit(enemy2_img, (x,y))

score = 0
is_jumping = False
jump_velocity = 0
gravity = 0.5
jump_strength = -10 
running=True
while running:
    clock.tick(FPS)

    all_time=time.time() -start
    screen.fill((30, 30, 30))
    timer_text = font.render(show_time(all_time), True, (0, 255, 0))
    # screen.blit(timer_text, (375, 20))

    enemyX -= 6
    enemy2X -= 6

    score += 0.1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not is_jumping:
                is_jumping = True
                jump_velocity = jump_strength
    if is_jumping:
        playerY += jump_velocity
        jump_velocity  += gravity

        if playerY >= playerY_ground:
            playerY = playerY_ground
            is_jumping = False
            jump_velocity = 0
    


    if playerX <= 0:
        playerX = 0
    elif playerX >=750:
        playerX = 0

    if enemyX <=0:
        enemyX = 750
    elif enemyX >=750:
        enemyX = 0

    if enemy2X <=0:
        enemy2X = 750
    elif enemy2X >=750:
        enemy2X = 0


    
    player(playerX,playerY)
    enemy(enemyX,enemyY)
    enemy2(enemy2X,enemy2Y)
    show_score(textX, textY, score)

    over=True

        

    

    pygame.display.update()

pygame.quit()
