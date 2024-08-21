import pygame
import random

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen1):
            pygame.draw.circle(center=self.position, radius=self.radius, width=2, color="white", surface=screen1)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        angle = random.uniform(20, 50)
        angle1, angle2 = self.velocity.rotate(angle), self.velocity.rotate(-angle)
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
        else:
            asteroid1 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
            asteroid2 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
            asteroid1.velocity = angle1 * 1.2
            asteroid2.velocity = angle2 * 1.2



