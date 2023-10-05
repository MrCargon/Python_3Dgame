from settings import *

text_map = [
    '111111111111',
    '1..2.....2.1',
    '1.2.11.12..1',
    '1..1.1.1..21',
    '12...11.2..1',
    '1..2..1.12.1',
    '1..........1',
    '111111111111'
]

world_enviroment = {}
mini_map = set()
for j, row in enumerate(text_map):
    for i, char in enumerate(row):
         if char != '.':
            mini_map.add((i * MAP_TILE, j * MAP_TILE))
            if char == '1':
                world_enviroment[(i * TILE_SIZE, j * TILE_SIZE)] = '1'
            elif char == '2':
                world_enviroment[(i * TILE_SIZE, j * TILE_SIZE)] = '2'