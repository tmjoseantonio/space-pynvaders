class Player(object):
    velocity = 50
    pos_x = 0
    pos_y = 0
    color = (0,255,0)
    width = 80
    height = 50

    def __init__(
        self,
        pos_x,
        pos_y
    ):
        self.pos_x = pos_x
        self.pos_y = pos_y

    def move_x(self, go_right):
        if go_right:
            self.pos_x += self.velocity
        else:
            self.pos_x -= self.velocity

    def get_player_shape(self):
        accurate_pos_y = self.pos_y - self.height

        return (
            (self.pos_x, accurate_pos_y + 50),
            (self.pos_x + 80, accurate_pos_y + 50),
            (self.pos_x + 80, accurate_pos_y + 35),
            (self.pos_x + 75, accurate_pos_y + 35),
            (self.pos_x + 75, accurate_pos_y + 30),
            (self.pos_x + 55, accurate_pos_y + 30),
            (self.pos_x + 55, accurate_pos_y + 15),
            (self.pos_x + 50, accurate_pos_y + 15),
            (self.pos_x + 42, accurate_pos_y + 15),
            (self.pos_x + 42, accurate_pos_y),
            (self.pos_x + 38, accurate_pos_y),
            (self.pos_x + 38, accurate_pos_y + 15),
            (self.pos_x + 25, accurate_pos_y + 15),
            (self.pos_x + 25, accurate_pos_y + 30),
            (self.pos_x + 5, accurate_pos_y + 30),
            (self.pos_x + 5, accurate_pos_y + 35),
            (self.pos_x, accurate_pos_y + 35)
        )