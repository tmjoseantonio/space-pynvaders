class Invader(object):
    velocity = 64

    def __init__(
        self,
        enemy_type,
        hp,
        pos_x,
        pos_y,
        sprites
    ):
        self.enemy_type = enemy_type
        self.hp = hp
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.sprites = sprites

    def move_x(self, go_right):
        if go_right:
            self.pos_x += self.velocity
        else:
            self.pos_x -= self.velocity

    def move_y(self):
        self.pos_y += self.velocity

    def get_movement_sprite(self, is_moving):
        return self.sprites[1] if is_moving else self.sprites[0]

    def get_next_pos_x(self):
        return self.pos_x + self.velocity
