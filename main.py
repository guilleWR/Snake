import pygame
from snake import Snake

pygame.init()

# Window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
COLOR_BACKGROUND = (128,128,128)

# Snake info
COLOR_SNAKE = (57, 255, 20)
head_size = 20
pos_x = 100
pos_y = 100

snake = Snake(COLOR_SNAKE, head_size, pos_x, pos_y)

MOVE_EVENT = pygame.event.custom_type()
pygame.time.set_timer(MOVE_EVENT, 150)

new_snake_direction = "none"

running = True
while running:
   
    for event in pygame.event.get():
        if event.type == MOVE_EVENT:
            snake.move_towards(new_snake_direction)
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                new_snake_direction = "down"
            if event.key == pygame.K_UP:
                new_snake_direction = "up"
            if event.key == pygame.K_LEFT:
                new_snake_direction = "left"
            if event.key == pygame.K_RIGHT:
                new_snake_direction = "right"

        
    screen.fill(COLOR_BACKGROUND)

    pygame.draw.rect(screen, snake.get_color(), snake.get_snake_rect())
    pygame.display.update()

    clock.tick(60)  

pygame.quit()