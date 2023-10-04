import pygame
from settings import *
from map_enviroment import world_enviroment

# Mapping
def mapping(a,b):
    return (a//TILE_SIZE*TILE_SIZE,(b//TILE_SIZE)*TILE_SIZE)
# New Ray cast System
def ray_casting(sc,player_pos, player_angle):
    ox, oy = player_pos
    xm, ym = (ox//TILE_SIZE) * TILE_SIZE, (oy//TILE_SIZE)*TILE_SIZE
    cur_angle = player_angle - HALF_FOV
    for ray in range(NUM_RAYS):
        sin_a = math.sin(cur_angle)
        cos_a = math.cos(cur_angle)

        # vertical itterator function
        x, dx = (xm + TILE_SIZE, 1) if cos_a >= 0 else (xm, -1)
        for i in range(0, WIDTH, TILE_SIZE):
            depth_v = (x - ox) / cos_a
            y = oy + depth_v * sin_a
            if mapping(x + dx, y) in world_enviroment:
                break
            x += dx * TILE_SIZE

        # horizontals
        y, dy = (ym + TILE_SIZE, 1) if sin_a >= 0 else (ym, -1)
        for i in range(0, HEIGHT, TILE_SIZE):
            depth_h = (y - oy) / sin_a
            x = ox + depth_h * cos_a
            if mapping(x, y + dy) in world_enviroment:
                break
            y += dy * TILE_SIZE
        
        # projection
        depth = depth_v if depth_v < depth_h else depth_h
        depth *= math.cos(player_angle - cur_angle)
        try:
            proj_height = PROJ_COEFF / depth
        except ZeroDivisionError:
            depth = 0.00001
            proj_height = PROJ_COEFF / depth
        c = 225/(1+depth*depth*0.0001)
        color=(c,c//2,c//3)
        pygame.draw.rect(sc,color,(ray*SCALE,HALF_HEIGHT-proj_height//2,SCALE,proj_height))
        cur_angle += DELTA_ANGLE

# Old NOT efficient raycast system
#def ray_casting(sc,player_pos,player_angle):
#    cur_angle = player_angle - HALF_FOV
#    xo, yo = player_pos
#    for ray in range(NUM_RAYS):
#        sin_a = math.sin(cur_angle)
#        cos_a = math.cos(cur_angle)
#        for depth in range(MAX_DEPTH):
#            depth += 0.0002
#            x = xo + depth * cos_a
#            y = yo + depth * sin_a
#            #pygame.draw.line(sc,DARKGRAY,player_pos,(x,y),2)
#            if (x//TILE_SIZE*TILE_SIZE,y//TILE_SIZE*TILE_SIZE) in world_enviroment:
#                depth *= math.cos(player_angle - cur_angle)
#                proj_height = PROJ_COEFF / depth
#                c = 225/(1+depth*depth*0.0001)
#                color=(c,c//2,c//3)
#                pygame.draw.rect(sc,color,(ray*SCALE,HALF_HEIGHT-proj_height//2,SCALE,proj_height))
#                break
#        cur_angle += DELTA_ANGLE