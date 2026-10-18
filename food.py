from pygame import Rect

class Food:

    # Posible implementacion de interfaz

    def __init__(self, head_size: float, pos_x: float, pos_y: float):
        self.color = (255, 0, 0)
        self.head_size = head_size
        self.pos_x = pos_x
        self.pos_y = pos_y

    def get_rect(self) -> Rect:
        return Rect(self.pos_x, self.pos_y, self.head_size, self.head_size)

    def get_pos_x(self) -> int:
        return self.pos_x
    
    def get_pos_y(self) -> int:
        return self.pos_y

    def set_pos_x(self, x: int) -> None:
        self.pos_x = x
        
    def set_pos_y(self, y: int) -> None:
        self.pos_y = y

    def get_color(self) -> tuple[int,int,int]:
        return self.color
    