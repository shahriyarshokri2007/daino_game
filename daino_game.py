import pygame
import time

pygame.init()

screen = pygame.display.set_mode((800,560))
font = pygame.font.Font(None, 36)
big_font = pygame.font.Font(None, 74)

background = pygame.image.load('background.png')

pygame.display.set_caption('Dinogame')
icon = pygame.image.load('daino.png')
pygame.display.set_icon(icon)

player_img = pygame.image.load('daino.png')
playerX=1
playerY=470
playerY_ground=470

enemy_img = pygame.image.load('enemy.png')
enemyX=800
enemyY=470

enemy2_img = pygame.image.load('enemy2.png')
enemy2X=400
enemy2Y=470


clock = pygame.time.Clock()
FPS = 60


font = pygame.font.Font('freesansbold.ttf',34)
textX=340
textY=10

over_font = pygame.font.Font("freesansbold.ttf",32)

def show_score(x,y,score):
    rounded_score = round(score)
    score_text = font.render("Score: " + str(rounded_score), True, (255,255,255))
    screen.blit(score_text, (x,y))

def game_over():
    over_text = over_font.render("GAME OVER", True, (255,0,0))
    screen.blit(over_text, (300,230))


def show_game_over_screen(final_score):
    screen.fill((255, 255, 255))
    screen.blit(background,(0,0))
    game_over()
    
    final_score_text = font.render("Final Score: " + str(round(final_score)), True, (255, 0, 0))
    screen.blit(final_score_text, (280, 280))
    # print(round(score))
    
    restart_text = font.render("Press SPACE to Restart", True, (0, 255, 0))
    screen.blit(restart_text, (230, 330))
    
    pygame.display.update()

def check_collision(player_x, player_y, enemy_x, enemy_y, enemy2_x, enemy2_y):
    player_rect = pygame.Rect(player_x, player_y, player_img.get_width(), player_img.get_height())
    enemy_rect = pygame.Rect(enemy_x, enemy_y, enemy_img.get_width(), enemy_img.get_height())
    enemy2_rect = pygame.Rect(enemy2_x, enemy2_y, enemy2_img.get_width(), enemy2_img.get_height())
    
    return player_rect.colliderect(enemy_rect) or player_rect.colliderect(enemy2_rect)

def reset_game():
    global playerX, playerY, enemyX, enemyY, enemy2X, enemy2Y, score, start, is_jumping, jump_velocity
    playerX = 1
    playerY = 470
    enemyX = 800
    enemyY = 470
    enemy2X = 400
    enemy2Y = 470
    score = 0
    start = time.time()
    is_jumping = False
    jump_velocity = 0

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
jump_strength = -12
running = True
game_active = True 

while running:
    clock.tick(FPS)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if game_active and not is_jumping:
                    is_jumping = True
                    jump_velocity = jump_strength
                elif not game_active:
                    reset_game()
                    game_active = True
    
    if game_active:
        all_time = time.time() - start
        screen.fill((255, 255, 255))
        screen.blit(background,(0,0))
        
        enemyX -= 6
        enemy2X -= 6
        
        score += 0.1
        
        if is_jumping:
            playerY += jump_velocity
            jump_velocity += gravity
            
            if playerY >= playerY_ground:
                playerY = playerY_ground
                is_jumping = False
                jump_velocity = 0
        
 
        if enemyX <= -100:  
            enemyX = 800
        if enemy2X <= -100:
            enemy2X = 800
        
        player(playerX,playerY)
        enemy(enemyX,enemyY)
        enemy2(enemy2X,enemy2Y)
        show_score(textX, textY, score)
        
        if check_collision(playerX, playerY, enemyX, enemyY, enemy2X, enemy2Y):
            game_active = False 
        
        pygame.display.update()
    
    else:
        show_game_over_screen(score)


pygame.quit()