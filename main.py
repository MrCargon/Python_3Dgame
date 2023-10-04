import pygame
from settings import *
from util_tools.entity import Entity
import math
from map_enviroment import world_enviroment
from util_tools.vision_raycasting import ray_casting
from util_tools.enviroment_drawing import Drawing
# Initialize pygame 
pygame.init()
# Create screen surface
sc = pygame.display.set_mode((WIDTH,HEIGHT))
# Minimap
sc_map = pygame.Surface((WIDTH//MAP_SCALE,HEIGHT//MAP_SCALE))
# Create clock for framerate
clock = pygame.time.Clock()
# Create player instance
player = Entity()
# Drawing Tool
drawing = Drawing(sc,sc_map)
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
    # pygame.draw.rect(sc,SKYBLUE,(0,0,WIDTH,HALF_HEIGHT))
    # Draw ground
    # pygame.draw.rect(sc,DARKGRAY,(0,HALF_HEIGHT,WIDTH,HALF_HEIGHT))
    # New draw tool draw background
    drawing.background()
    # New Drawing tool use not the ray cast
    drawing.world(player.pos,player.angle)
    # Draw FPS
    drawing.fps(clock)
    # Old Do ray casting
    # ray_casting(sc,player.pos,player.angle)
    # Draw player circle
    # pygame.draw.circle(sc,GREEN,(int(player.x),int(player.y)),12)
    # Draw player fov line
    # pygame.draw.line(sc,GREEN, player.pos, (player.x + WIDTH * math.cos(player.angle),
    #                                        player.y + WIDTH * math.sin(player.angle)))
    # Draw world rects
    # for x,y in world_enviroment:
    #    pygame.draw.rect(sc, DARKGRAY, (x,y,TILE_SIZE,TILE_SIZE),2)
    
    # Drawing MiniMap
    drawing.mini_map(player)
    
    # Update display
    pygame.display.flip()
    # Set framerate
    clock.tick()