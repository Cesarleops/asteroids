import pygame

class CircleShape(pygame.sprite.Sprite):
    def __init__(self,x,y,radius):
        if hasattr(self,'containers'):
            super().__init__(self.containers)
        else:
            super().__init__()
        
        self.position = pygame.Vector2(x,y)

        #Velocity is 0 at first, the player isn't moving in any direction and has no speed.
        self.velocity = pygame.Vector2(0,0)
        self.radius = radius

    def draw(self, screen):

        # sub-classes must override
            pass

    def update(self, dt):
        # sub-classes must override
            pass

    def is_colliding(self,circle_shape):

            distance = self.position.distance_to(circle_shape.position)

            collision_detected = distance <= (self.radius + circle_shape.radius)

            return collision_detected