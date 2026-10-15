import pygame
from pygame import Rect
from snake import Snake

pygame.init()

# Window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

COLOR_SNAKE = (57, 255, 20)
HEAD_SIZE = 20

def _snake_is_outside(snake: Snake) -> bool:
    snake_rect = snake.get_rect()
    return (snake_rect.left < 0) or (snake_rect.right > SCREEN_WIDTH) or (snake_rect.top < 0) or (snake_rect.bottom > SCREEN_HEIGHT)

def move_and_update_position(snake: Snake, direcion: str) -> None:
    snake.set_previous_position(snake.get_pos_x(), snake.get_pos_y())
    snake.move_towards(direcion)
    snake.set_current_position(snake.get_pos_x(), snake.get_pos_y())
    # Update Body

    
    for child in snake.get_childs():
        # obtain dad from child...

        # antes cuando esté la funcion create_child, se hara un snake nuevo para que no falle esta parte
        child.set_previous_position(child.get_pos_x(), child.get_pos_y()) 
        tp = snake.get_previous_position()
        child.set_current_position(tp[0], tp[1])
        

    print("Current: " + str(snake.get_current_position()) + " --- " + "Previous: " + str(snake.get_previous_position()) + "\n")
    print("Current child: " + str(child.get_current_position()) + " --- " + "Previous child: " + str(child.get_previous_position()))
    print("\n-------------------------------")

def init_child_list(snake: Snake):
    snake_child = Snake(COLOR_SNAKE, HEAD_SIZE, 0, 0)
    snake.add_child(snake_child)

def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    COLOR_BACKGROUND = (128,128,128)

    # Snake info
    pos_x = 0
    pos_y = 0
    snake = Snake(COLOR_SNAKE, HEAD_SIZE, pos_x, pos_y)

    init_child_list(snake)

    MOVE_EVENT = pygame.event.custom_type()
    pygame.time.set_timer(MOVE_EVENT, 150)

    new_snake_direction = "none"

    running = True
    while running:
        
        for event in pygame.event.get():
            if event.type == MOVE_EVENT:
                #Ojo esto no me vale para los hijos porque tienen que moverse solo hacia el previous de su padre  (nada con directions)
                move_and_update_position(snake, new_snake_direction)

                
                if _snake_is_outside(snake):
                    running = False

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

        pygame.draw.rect(screen, snake.get_color(), snake.get_rect())

        
        for child in snake.get_childs():
            pygame.draw.rect(screen, child.get_color(), child.get_rect())

        pygame.display.update()

        clock.tick(60)  

    pygame.quit()

if __name__ == "__main__":
    main()