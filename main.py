import pygame
from settings import *
from util_tools.entity import Entity
import math
from map_enviroment import world_enviroment
from util_tools.vision_raycasting import ray_casting
# Initialize pygame 
pygame.init()
# Create screen surface
sc = pygame.display.set_mode((WIDTH,HEIGHT))
# Create clock for framerate
clock = pygame.time.Clock()
# Create player instance
player = Entity()
# Main game loop
while True:
    # Check for quit event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    # Update player position 
    player.update()
    # Fill background
    sc.fill(BLACK)
    # Draw sky
    pygame.draw.rect(sc,BLUE,(0,0,WIDTH,HALF_HEIGHT))
    # Draw ground
    pygame.draw.rect(sc,DARKGRAY,(0,HALF_HEIGHT,WIDTH,HALF_HEIGHT))
    # Do ray casting
    ray_casting(sc,player.pos,player.angle)
    # Draw player circle
    # pygame.draw.circle(sc,GREEN,(int(player.x),int(player.y)),12)
    # Draw player fov line
    # pygame.draw.line(sc,GREEN, player.pos, (player.x + WIDTH * math.cos(player.angle),
    #                                        player.y + WIDTH * math.sin(player.angle)))
    # Draw world rects
    # for x,y in world_enviroment:
    #    pygame.draw.rect(sc, DARKGRAY, (x,y,TILE_SIZE,TILE_SIZE),2)
    # Update display
    pygame.display.flip()
    # Set framerate
    clock.tick(FPS)