# haha the play urr lives here

import math
from tzmath import radToDeg, degToRad
import pygame

class Player:
    def __init__(self):
        self.x = 0     # positional data
        self.y = 0
        self.z = 0
        self.dx= 0     # velocity
        self.dy= 0
        self.dz= 0
        self.sp= 0     # speed
        self.gr= 0     # gravity
        self.fr= 0     # friction
        self.a = 0     # yaw
        self.l = 0     # pitch
        self.r = 0     # roll (probably will be unused but maybe ill use it for a screen shake or smth)
    
    def pUp(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.a -= 4
        if keys[pygame.K_d]:
            self.a += 4
            
        if self.a > 359:
            self.a -= 360
        if self.a < 0:
            self.a += 360
        
        if keys[pygame.K_w]:
            self.dx+= math.cos(self.a)
            self.dy+= math.sin(self.a)
        if keys[pygame.K_s]:
            self.dx-= math.cos(self.a)
            self.dy-= math.sin(self.a)