import sys
import pygame
from asteroid import Asteroid
from asteroidfield import AsteroidField
from player import *
from constants import *


updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
bullets = pygame.sprite.Group()

Player.containers = (updatable, drawable)
Asteroid.containers = (updatable, drawable, asteroids)
AsteroidField.containers = updatable
Shot.containers = (bullets, drawable, updatable)

def main():
    pygame.init()
    dt = 0
    clock = pygame.time.Clock()
    screen1 = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    stop = False
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    afield = AsteroidField()


    while not stop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen1.fill(color="black")
        for i in updatable:
            i.update(dt)
        for i in drawable:
            i.draw(screen1)
        for i in asteroids:
            if i.collision(player):
                print("Game Over!")
                sys.exit()
            for b in bullets:
                if i.collision(b):
                    i.split()
                    b.kill()

        pygame.display.flip()
        dt = clock.tick(60) /1000


if __name__ == "__main__":
    main()