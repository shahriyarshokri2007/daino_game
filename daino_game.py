import pygame

pygame.init()

screen = pygame.display.set_mode((800,600))

pygame.display.set_caption('Dinogame')
icon = pygame.image.load('daino.png')
pygame.display.set_icon(icon)

player_img = pygame.image.load('daino.png')
playerX=1
playerY=300


def player(x,y):
    screen.blit(player_img, (x,y))

counter=0
running=True
while running:

    screen.fill((30,30,30))
    playerX += 0.1
    counter+=1
    if counter == 7914:
        playerX == 1
        continue
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    player(playerX,playerY)
    pygame.display.update()