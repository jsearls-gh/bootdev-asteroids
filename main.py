import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            return

        screen.fill("black")

        for element in updatable:
            element.update(dt)

        for asteroid in asteroids:
            if(player.has_collided_with(asteroid)):
               print("Game Over!")
               exit(0)

            for shot in shots:
                if asteroid.has_collided_with(shot):
                    shot.kill()
                    asteroid.split()

        for element in drawable:
            element.draw(screen)

        pygame.display.flip()
        dt_ms = clock.tick(60)
        dt = dt_ms / 1000

if __name__ == "__main__":
    main()
