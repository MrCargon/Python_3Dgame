from settings import *

text_map = [
    'wwwwwwwwwwww',
    'w..........w',
    'w.w.ww.ww..w',
    'w..w.w.w..ww',
    'ww...ww.w..w',
    'w..w..w.ww.w',
    'w..........w',
    'wwwwwwwwwwww'
]

world_enviroment = set()
for j, row in enumerate(text_map):
    for i, char in enumerate(row):
        if char == 'w':
            world_enviroment.add((i * TILE_SIZE, j * TILE_SIZE))