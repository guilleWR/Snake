from pygame import Rect

class Snake:

    def __init__(self, color: tuple[int,int,int],  head_size: float, pos_x: float, pos_y: float):
        self.color = color
        self.head_size = head_size
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.current_direction = "none"


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
            running = False
        
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