import pygame
import random
import time

# Game Constants
WIDTH = 800
HEIGHT = 600
SNAKE_BLOCK = 20
FOOD_BLOCK = 20

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Display Setup will be initialized inside start_game()
screen = None
clock = None
font = None

def init_game():
    global screen, clock, font
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Snake Game")
    clock = pygame.time.Clock()
    try:
        font = pygame.font.SysFont("Outfit", 35)
    except:
        font = pygame.font.SysFont(None, 35)

def show_score(score):
    if font:
        value = font.render("Score: " + str(score), True, WHITE)
        screen.blit(value, [10, 10])

def game_loop():
    game_over = False
    game_close = False

    # Snake initial position
    x = WIDTH / 2
    y = HEIGHT / 2

    # Initial velocity
    dx = 0
    dy = 0

    snake_list = []
    snake_length = 1

    # Food initial position (aligned to grid)
    food_x = round(random.randrange(0, WIDTH - FOOD_BLOCK) / 20.0) * 20.0
    food_y = round(random.randrange(0, HEIGHT - FOOD_BLOCK) / 20.0) * 20.0

    score = 0

    while not game_over:

        while game_close:
            screen.fill(BLACK)
            msg = font.render("Game Over! Press Q-Quit or C-Play Again", True, RED)
            screen.blit(msg, [WIDTH / 6, HEIGHT / 3])
            show_score(score)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and dx == 0:
                    dx = -SNAKE_BLOCK
                    dy = 0
                elif event.key == pygame.K_RIGHT and dx == 0:
                    dx = SNAKE_BLOCK
                    dy = 0
                elif event.key == pygame.K_UP and dy == 0:
                    dy = -SNAKE_BLOCK
                    dx = 0
                elif event.key == pygame.K_DOWN and dy == 0:
                    dy = SNAKE_BLOCK
                    dx = 0

        # Boundary Check
        if x >= WIDTH or x < 0 or y >= HEIGHT or y < 0:
            game_close = True

        x += dx
        y += dy
        
        screen.fill(BLACK)
        
        # Draw Food
        pygame.draw.rect(screen, RED, [food_x, food_y, FOOD_BLOCK, FOOD_BLOCK])
        
        # Update Snake Body
        snake_head = [x, y]
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        # Self Collision Check
        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_close = True

        # Draw Snake
        for segment in snake_list:
            pygame.draw.rect(screen, GREEN, [segment[0], segment[1], SNAKE_BLOCK, SNAKE_BLOCK])

        show_score(score)
        pygame.display.update()

        # Food Collision Check
        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, WIDTH - FOOD_BLOCK) / 20.0) * 20.0
            food_y = round(random.randrange(0, HEIGHT - FOOD_BLOCK) / 20.0) * 20.0
            snake_length += 1
            score += 10

        clock.tick(15)

    pygame.quit()
    quit()

def start_game():
    init_game()
    game_loop()

if __name__ == "__main__":
    start_game()