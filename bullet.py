import pygame
from circleshape import CircleShape


class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen1):
        pygame.draw.circle(center=self.position, radius=self.radius, width=2, color="white", surface=screen1)

    def update(self, dt):
        self.position += self.velocity * dt