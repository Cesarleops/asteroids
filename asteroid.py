import pygame
import random 
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, ASTEROID_MAX_RADIUS, ASTEROID_KINDS


class Asteroid(CircleShape):
    def __init__(self,x,y,radius):
        super().__init__(x,y,radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen,'white',self.position,self.radius, 2)

    def update(self,dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        spawn_angle = random.uniform(20,50)

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid_1_v =  self.velocity.rotate(spawn_angle)

        asteroid_2_v = self.velocity.rotate(-spawn_angle)

        asteroid_1 = Asteroid(self.position.x,self.position.y,new_radius)
        asteroid_1.velocity = asteroid_1_v * 1.2

        asteroid_2 = Asteroid(self.position.x,self.position.y,new_radius)
        asteroid_2.velocity = asteroid_2_v * 1.2
