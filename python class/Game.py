import pygame
import random

pygame.init()

WIDTH, HEIDHT = 800, 600

screen = pygame.display.set_mode((WIDTH, HEIDHT))
pygame.display.set_caption("Catch the Falling Blocks")

WHITE = (255,255,255)
BLUE = (50,150,255)
RED = (255,80,80)
BLACK = (0,0,0)

clock = pygame.time.Clock()

player_width = 100
player_height = 20
player_x = WIDTH //2 - player_width //2
player_y = HEIDHT - 50
player_speed = 7

block_size=30
block_x = random.randint (0, WIDTH-block_size)
block_y =- block_size
block_speed=5

score=0
font = pygame.font.SysFont (None , 36)

running = True
while running:
    clock.tick(60)
    screen.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x >0:
        player_x -=player_speed
    if keys [pygame.K_RIGHT] and player_x <WIDTH - player_width:
        player_x += player_speed

    block_y +=block_speed

    if block_y > HEIDHT:
        block_x = random.randint (0, WIDTH - block_size)
        block_y =-block_size

    player_rect = pygame.Rect(player_x,player_y, player_width,player_height)
    block_rect = pygame.Rect(block_x,block_y,block_size,block_size)
    if player_rect.colliderect(block_rect):
        score +=1
        block_x = random.randint(0,WIDTH - block_size)
        block_y =-block_size

    pygame.draw.rect(screen, BLUE, player_rect)

    pygame.draw.rect(screen,RED, block_rect)

    score_text = font.render(f"score:{score}",True, BLACK)
    screen.blit(score_text,(10,10))

    pygame.display.flip()
pygame.quit()
