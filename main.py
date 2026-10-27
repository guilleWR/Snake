import pygame
from pygame import Rect
from snake import Snake, Node
from food import Food

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

HEAD_SIZE = 20
COLOR_SNAKE = (57, 255, 20)
COLOR_BACKGROUND = (128,128,128)

text_font = pygame.font.SysFont("Arial", 15)

def _snake_is_outside(snake: Snake) -> bool:
    snake_rect = snake.get_rect()
    return (snake_rect.left < 0) or (snake_rect.right > SCREEN_WIDTH) or (snake_rect.top < 0) or (snake_rect.bottom > SCREEN_HEIGHT)

def _snake_touches_tail(snake: Snake) -> bool:
    for node in snake.get_childs():
        if snake.get_size() > 3 and node.get_child().get_rect().center == snake.get_rect().center:
            return True
    return False

def move_and_update_position(snake: Snake, direcion: str) -> None:
    snake.set_previous_position(snake.get_pos_x(), snake.get_pos_y())
    snake.move_towards(direcion)
    snake.set_current_position(snake.get_pos_x(), snake.get_pos_y())
    
    for node in snake.get_childs():
        child = node.get_child()
        dad = node.get_dad()

        child.set_previous_position(child.get_pos_x(), child.get_pos_y()) 
        tp = dad.get_previous_position()
        child.set_current_position(tp[0], tp[1])
        
def init_child_list(snake: Snake):
    snake_child1 = Snake(COLOR_SNAKE, HEAD_SIZE, 0, 0)
    snake_child2 = Snake(COLOR_SNAKE, HEAD_SIZE, 0, 0)

    node1 = Node(snake_child1, snake)
    node2 = Node(snake_child2, snake_child1)

    snake.set_child_list([node1,node2])
    snake.set_size(3) #cambiar por calcular lista

def draw_score(score, font, color, x, y):
    text = "Score: " + str(score)
    img = font.render(text, True, color)
    screen.blit(img, (x,y))

def main():
    score = 0
    clock = pygame.time.Clock()
    
    # Snake info
    pos_x = 0
    pos_y = 0
    snake = Snake(COLOR_SNAKE, HEAD_SIZE, pos_x, pos_y)

    apple = Food(HEAD_SIZE, int(SCREEN_WIDTH), int(SCREEN_HEIGHT))
    init_child_list(snake)

    MOVE_EVENT = pygame.event.custom_type()
    pygame.time.set_timer(MOVE_EVENT, 100)
    
    new_snake_direction = "none"
    running = True
    while running:
        
        for event in pygame.event.get():
            if event.type == MOVE_EVENT:
                move_and_update_position(snake, new_snake_direction)
                screen.fill(COLOR_BACKGROUND)
                draw_score(score, text_font, (0,0,0), 720, 10)

                if _snake_is_outside(snake) or _snake_touches_tail(snake):
                    running = False

                if snake.get_rect().center == apple.get_rect().center:
                    apple.updateCoordinates()
                    score = score + 1
                    last_node = snake.get_childs()[-1]
                    future_dad = last_node.get_child()
                    snake.add_child(future_dad) 

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
            
        pygame.draw.rect(screen, snake.get_color(), snake.get_rect())
        pygame.draw.rect(screen, apple.get_color(), apple.get_rect())
        
        for node in snake.get_childs():
            child = node.get_child()
            pygame.draw.rect(screen, child.get_color(), child.get_rect())

        #pygame.display.update()
        pygame.display.flip()
        clock.tick(60)  

    pygame.quit()

if __name__ == "__main__":
    main()