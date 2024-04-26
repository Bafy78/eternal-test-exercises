class Tortue:
    x = 0
    y = 0
    direction = "D"
    
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def look_down(self):
        self.direction = "D"

    def look_right(self):
        self.direction = "R"

    def look_up(self):
        self.direction = "U"

    def look_left(self):
        self.direction = "L"

    def walk(self, n):
        if self.direction == "D":
            self.y += n
        if self.direction == "R":
            self.x += n
        if self.direction == "U":
            self.y -= n
        if self.direction == "L":
            self.x -= n

    def teleport(self, x, y):
        self.x = x
        self.y = y