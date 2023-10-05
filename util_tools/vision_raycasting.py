import pygame
from settings import *
from map_enviroment import world_enviroment

# Mapping
def mapping(a,b):
    return (a//TILE_SIZE*TILE_SIZE,(b//TILE_SIZE)*TILE_SIZE)
# New Ray cast System
def ray_casting(sc,player_pos, player_angle,textures):
    # Initialize to prevent unbound errors
    texture_v = None
    texture_h = None
    # Current player position and angle
    ox, oy = player_pos
    xm, ym = mapping(ox, oy)
    cur_angle = player_angle - HALF_FOV
    # Ray casting loop
    for ray in range(NUM_RAYS):
        # Calculate ray direction
        sin_a = math.sin(cur_angle)
        cos_a = math.cos(cur_angle)
        # Fixdiv by zero errors
        sin_a = sin_a if sin_a else 0.000001
        cos_a = cos_a if cos_a else 0.000001
        # Vertical intersection
        x, dx = (xm + TILE_SIZE, 1) if cos_a >= 0 else (xm, -1)
        for i in range(0, WIDTH, TILE_SIZE):
            # Calc depth and position
            depth_v = (x - ox) / cos_a
            yv = oy + depth_v * sin_a
            # Map to tile
            tile_v = mapping(x + dx, yv)
            # Check for map collision
            if tile_v in world_enviroment:
                # Set vertical texture on hit
                texture_v = world_enviroment[tile_v]
                # Break vertical loop
                break
            # Increment x
            x += dx * TILE_SIZE
        # Horizontal intersection
        y, dy = (ym + TILE_SIZE, 1) if sin_a >= 0 else (ym, -1)
        for i in range(0, HEIGHT, TILE_SIZE):
            # Calc depth and position
            depth_h = (y - oy) / sin_a
            xh = ox + depth_h * cos_a
            # Map to tile
            tile_h = mapping(xh, y + dy)
            # Check for map collision
            if tile_h in world_enviroment:
                # Set horizontal texture on hit
                texture_h = world_enviroment[tile_h]
                # Break horizontal loop
                break
            # Increment y
            y += dy * TILE_SIZE
        # Choose vertical or horizontal hit
        depth, offset, texture = (depth_v, yv, texture_v) if depth_v < depth_h else (depth_h, xh, texture_h)
        # Wrap offset to texture width 
        offset = int(offset) % TILE_SIZE
        depth *= math.cos(player_angle - cur_angle)
        depth = max(depth,0.00001)
        proj_height = min(int(PROJ_COEFF / depth),2*HEIGHT)
        #
        wall_column = textures[texture].subsurface(offset * TEXTURE_SCALE, 0, TEXTURE_SCALE, TEXTURE_HEIGHT)
        wall_column = pygame.transform.scale(wall_column, (SCALE, proj_height))
        sc.blit(wall_column, (ray * SCALE, HALF_HEIGHT - proj_height // 2))
        #
        cur_angle += DELTA_ANGLE
