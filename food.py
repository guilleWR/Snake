from pygame import Rect
import random

class Food:

    # Recibir maximos de la pantalla X, Y para calcular posicion aleatoria

    # Posible implementacion de interfaz

    def __init__(self, head_size: float, x: int, y: int):
        self.color = (255, 0, 0)
        self.head_size = head_size
        self.max_x = x
        self.max_y = y
        self.pos_x = self.random_even(x)
        self.pos_y = self.random_even(y)


    def random_even(self, max_size) -> int:
        is_even = False
        while not is_even: 
            res = random.randint(0, max_size - self.head_size)
            if res % 20 == 0:
                return res

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

    def updateCoordinates(self) -> None:
        self.pos_x = self.random_even(self.max_x)
        self.pos_y = self.random_even(self.max_y)

    def show_coords(self) -> str:
        return "(" + str(self.pos_x) + "," + str(self.pos_y) + ")"