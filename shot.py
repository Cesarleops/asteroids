import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS

class Shot(CircleShape):
    def __init__(self,x,y):
            super().__init__(x,y, SHOT_RADIUS)

    def set_velocity(self,increment):
          self.velocity = increment


    def draw(self, screen):
        pygame.draw.circle(screen,'red',self.position,self.radius, 2)

    def update(self,dt):
        self.position += (self.velocity * dt)