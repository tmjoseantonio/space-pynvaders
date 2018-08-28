import os
import pygame
import random
from enemy import Invader

# Constants
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768
FPS = 60

# Enemy Array
ENEMIES_PER_ROW = 8
ENEMY_ROWS = 5
ENEMIES_DATA = {
    'alien-a': {
        'sprites': ['assets/alien-a-1.png', 'assets/alien-a-2.png']
    },
    'alien-b': {
        'sprites': ['assets/alien-b-1.png', 'assets/alien-b-2.png']
    },
    'alien-c': {
        'sprites': ['assets/alien-c-1.png', 'assets/alien-c-2.png']
    }
}
SHIP_SPRITE = 'assets/ship.png'

# Screen setup
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
done = False  # Exit condition

enemy_grid = []
enemy_row = []
row_x = 0
row_y = 0
ROW_Y_INCREMENT = 50
ROW_X_INCREMENT = 64
ENEMY_HP = 1
ENEMY_MOVEMENT_THRESHOLD = 500  # miliseconds

# Load enemy sprites
for enemy in ENEMIES_DATA:
    ENEMIES_DATA[enemy]['sprite'] = []
    for path in ENEMIES_DATA[enemy]['sprites']:
        ENEMIES_DATA[enemy]['sprite'].append(
            pygame.image.load(path).convert_alpha()
        )

ship = pygame.image.load(SHIP_SPRITE).convert_alpha()

# Game initialization
for row_count in range(0, ENEMY_ROWS):
    row_enemy_type = random.choice(list(ENEMIES_DATA.keys()))
    for enemy_count in range(0, ENEMIES_PER_ROW):
        enemy_row.append(
            Invader(
                row_enemy_type,
                ENEMY_HP,
                row_x,
                row_y,
                ENEMIES_DATA[row_enemy_type]['sprite']
            )
        )
        row_x += ROW_X_INCREMENT
        enemy_grid.append(enemy_row)
    row_x = 0
    row_y += ROW_Y_INCREMENT

# Custom events
ENEMY_MOVES = pygame.USEREVENT+1
pygame.time.set_timer(ENEMY_MOVES, ENEMY_MOVEMENT_THRESHOLD)

# Control variables
first_loop = True
enemy_update_sprite = False
enemy_should_move = False
move_right = True
move_bottom = False
last_enemy = enemy_grid[0][-1]
first_enemy = enemy_grid[0][0]
previously_moved_to_bottom = False

# Game loop
while not done:
    # Events
    for event in pygame.event.get():
        if event.type == ENEMY_MOVES:
            enemy_should_move = True
            enemy_update_sprite = not enemy_update_sprite

            # Find next position
            last_enemy_next_pos = last_enemy.get_next_pos_x()
            first_enemy_next_pos = first_enemy.get_next_pos_x()

            # Find if next movement is out of bounds
            is_first_out_of_x = first_enemy_next_pos <= ROW_X_INCREMENT
            is_last_out_of_x = SCREEN_WIDTH/last_enemy_next_pos == 1.00

            if not first_loop:
                if is_first_out_of_x and not previously_moved_to_bottom:
                    move_right = True
                    move_bottom = True
                elif is_last_out_of_x and not previously_moved_to_bottom:
                    move_right = False
                    move_bottom = True
                else:
                    move_bottom = False

            first_loop = False

        if event.type == pygame.QUIT:
            done = True

    # Reset screen
    screen.fill((0, 0, 0))

    for row in enemy_grid:
        for enemy in row:
            if enemy_should_move and move_bottom:
                enemy.move_y()
            elif enemy_should_move and not move_bottom:
                enemy.move_x(move_right)

            screen.blit(
                enemy.get_movement_sprite(enemy_update_sprite),
                (enemy.pos_x, enemy.pos_y)
            )
        enemy_should_move = False

    previously_moved_to_bottom = True if move_bottom else False

    # Extra stuff
    pygame.display.flip()
    clock.tick(FPS)
