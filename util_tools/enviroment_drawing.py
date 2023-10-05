import pygame
from settings import *
from util_tools.vision_raycasting import ray_casting
from map_enviroment import mini_map

class Drawing:
    def __init__(self,sc,sc_map) -> None:
        self.sc = sc
        self.sc_map = sc_map
        self.font = pygame.font.SysFont('Arial', 36, bold=True)
        self.texture = {'default': pygame.image.load('res/img/default.png'),
                        '1': pygame.image.load('res/img/white_rock_with_blue_wall.png').convert(),
                        '2': pygame.image.load('res/img/brown_brick_wall.png').convert(),
                        'S': pygame.image.load('res/img/blue_sky.png').convert()
                        }
    
    def background(self,angle):
        # New Sky
        sky_offset = -5*math.degrees(angle) % WIDTH
        self.sc.blit(self.texture['S'],(sky_offset,0))
        self.sc.blit(self.texture['S'],(sky_offset - WIDTH,0))
        self.sc.blit(self.texture['S'],(sky_offset + WIDTH,0))
        # Old Draw sky
        # pygame.draw.rect(self.sc,SKYBLUE,(0,0,WIDTH,HALF_HEIGHT))
        # Draw ground
        pygame.draw.rect(self.sc,DARKGRAY,(0,HALF_HEIGHT,WIDTH,HALF_HEIGHT))

    def world(self,player_pos, player_angle):
        ray_casting(self.sc,player_pos,player_angle,self.texture)

    def fps(self, clock):
        display_fps = str(int(clock.get_fps()))
        render = self.font.render(display_fps, 0, RED)
        self.sc.blit(render, FPS_POS)
    
    def mini_map(self, player):
        #
        self.sc_map.fill(BLACK)
        map_x, map_y = player.x // MAP_SCALE, player.y // MAP_SCALE
        # Draw player look at line
        pygame.draw.line(self.sc_map, YELLOW, (map_x, map_y), (map_x + 12 * math.cos(player.angle),
                                                 map_y + 12 * math.sin(player.angle)), 2)
        # Draw player as curcle
        pygame.draw.circle(self.sc_map, RED, (int(map_x), int(map_y)), 5)
        # Draw min map
        for x, y in mini_map:
            pygame.draw.rect(self.sc_map, SANDY, (x, y, MAP_TILE, MAP_TILE))
        self.sc.blit(self.sc_map, MAP_POS)