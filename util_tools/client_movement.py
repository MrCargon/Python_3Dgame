import pygame 
import math

def movement(entity, player_speed):
    
    sin_a = math.sin(entity.angle)
    cos_a = math.cos(entity.angle)
    
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_w]:
        entity.x += player_speed * cos_a
        entity.y += player_speed * sin_a

    if keys[pygame.K_s]:
        entity.x += -player_speed * cos_a
        entity.y += -player_speed * sin_a

    if keys[pygame.K_a]:
        entity.x += player_speed * sin_a
        entity.y += -player_speed * cos_a

    if keys[pygame.K_d]:
        entity.x += -player_speed * sin_a
        entity.y += player_speed * cos_a

    if keys[pygame.K_LEFT]:
        entity.angle -= 0.04

    if keys[pygame.K_RIGHT]:
        entity.angle += 0.04