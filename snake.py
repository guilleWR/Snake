from pygame import Rect

class Node:
    def __init__(self, child: Snake, dad: Snake):
        self.child = child
        self.dad = dad

    def get_child(self) -> Snake:
        return self.child

    def get_dad(self) -> Snake:
        return self.dad


class Snake:

    def __init__(self, color: tuple[int,int,int],  head_size: float, pos_x: float, pos_y: float):
        self.color = color
        self.head_size = head_size
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.size = 0
        self.current_direction = "none"
        self.current_position = (pos_x, pos_y)
        self.previous_position = self.current_position
        self.childs = [Node]


    def get_childs(self) -> list[Node]:
        return self.childs

    def get_color(self) -> tuple[int,int,int]:
        return self.color

    # Posible mejora, no crear un Rect nuevo cada vez
    def get_rect(self) -> Rect:
        return Rect(self.pos_x, self.pos_y, self.head_size, self.head_size)


    def move_towards(self, new_direction: str):  
        if new_direction == "right":
            if self.current_direction == "left":
                self._go_to(self.current_direction)
            else:
                self._go_to(new_direction)

        elif new_direction == "left":
            if self.current_direction == "right":
                self._go_to(self.current_direction)
            else:
                self._go_to(new_direction)
  
        elif new_direction == "up":
            if self.current_direction == "down":
                self._go_to(self.current_direction)
            else:
                self._go_to(new_direction)
          
        elif new_direction == "down":
            if self.current_direction == "up":
                self._go_to(self.current_direction)
            else:
                self._go_to(new_direction)
    

    def _go_to(self, direction: str):
        if direction == "left":
            self._move_left()

        if direction == "right":
            self._move_right()

        if direction == "up":
            self._move_up()

        if direction == "down":
            self._move_down()

        self.current_direction = direction

  # ----------------------------------
    def _move_down(self) -> None:
        self.pos_y += self.head_size

    def _move_up(self) -> None:
        self.pos_y -= self.head_size

    def _move_right(self) -> None:
        self.pos_x += self.head_size

    def _move_left(self) -> None:
        self.pos_x -= self.head_size
    # ----------------------------------

    def get_current(self):
            return self.current_direction

    def get_pos_x(self) -> int:
        return self.pos_x

    def get_pos_y(self) -> int:
        return self.pos_y

    def get_head_size(self) -> float:
        return self.head_size

    def get_head_cords(self) -> str:
        x = str(self.pos_x)
        y = str(self.pos_y)
        return "(" + x + "," + y + ")" 

    def get_tail(self) -> Snake:
        return self

    def get_current_position(self) -> tuple[float,float]:
        return self.current_position

    def get_previous_position(self) -> tuple[float,float]:
        return self.previous_position

    def set_previous_position(self, x: float, y: float) -> None:
        self.pos_x = x
        self.pos_y = y
        self.previous_position = (x,y)

    def set_current_position(self, x: float, y: float) -> None:
        self.pos_x = x
        self.pos_y = y
        self.previous_position = (x,y)

    def set_child_list(self, initial_childs: list[Node]):
        self.childs = initial_childs

    def add_child(self, dad: Snake) -> None:
        new_snake = Snake(self.color, self.head_size, dad.get_previous_position()[0], dad.get_previous_position()[1]) 
        new_node = Node(new_snake, dad)
        self.childs.append(new_node)
        self.size = self.size + 1

    def show_coords(self) -> str:
        return "(" + str(self.pos_x) + "," + str(self.pos_y) + ")"

    def set_size(self, x: int) -> None:
        self.size = x

    def get_size(self) -> int:
        return self.size