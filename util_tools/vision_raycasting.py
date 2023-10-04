import pygame
from settings import *
from map_enviroment import world_enviroment

def ray_casting(sc,player_pos,player_angle):
    cur_angle = player_angle - HALF_FOV
    xo, yo = player_pos
    for ray in range(NUM_RAYS):
        sin_a = math.sin(cur_angle)
        cos_a = math.cos(cur_angle)
        for depth in range(MAX_DEPTH):
            depth += 0.0001
            x = xo + depth * cos_a
            y = yo + depth * sin_a
            #pygame.draw.line(sc,DARKGRAY,player_pos,(x,y),2)
            if (x//TILE_SIZE*TILE_SIZE,y//TILE_SIZE*TILE_SIZE) in world_enviroment:
                depth *= math.cos(player_angle - cur_angle)
                proj_height = PROJ_COEFF / depth
                c = 225/(1+depth*depth*0.0001)
                color=(c//2,c,c//3)
                pygame.draw.rect(sc,color,(ray*SCALE,HALF_HEIGHT-proj_height//2,SCALE,proj_height))
                break
        cur_angle += DELTA_ANGLE