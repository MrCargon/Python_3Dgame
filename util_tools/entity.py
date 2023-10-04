import pygame
from settings import *
import math
from util_tools.client_movement import movement

class Entity:
    def __init__(self) -> None:
        self.x, self.y = player_pos
        self.angle = player_angle

    @property
    def pos(self):
        return (self.x, self.y)

    def update(self):
        movement(self, player_speed)