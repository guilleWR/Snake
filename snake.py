from pygame import Rect

class Snake:

    def __init__(self, color: tuple[int,int,int],  head_size: float, pos_x: float, pos_y: float):
        self.color = color
        self.head_size = head_size
        self.pos_x = pos_x
        self.pos_y = pos_y


    def get_color(self) -> tuple[int,int,int]:
        return self.color

    # Posible mejora, no crear un Rect nuevo cada vez
    def get_snake_rect(self) -> Rect:
        return Rect(self.pos_x, self.pos_y, self.head_size, self.head_size)


    # Posible mejora: hacer 1 unico metodo "move" y comprobar a donde tiene que ir
    
    def move_down(self) -> None:
        self.pos_y += self.head_size

    def move_up(self) -> None:
        self.pos_y -= self.head_size

    def move_right(self) -> None:
        self.pos_x += self.head_size

    def move_left(self) -> None:
        self.pos_x -= self.head_size