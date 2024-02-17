import pygame
from planets import Planet

WIDTH, HEIGHT = 800, 800

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Planet Simulation")

background_color = (255, 255, 255)  #WHITE
sun_color = (255, 255, 0)

def main():
    run = True
    clock = pygame.time.Clock()

    sun = Planet(0,0,30, sun_color, 1.98892 * 10 ** 30)
    sun.sun = True

    planets = [sun]

    while run:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        for planet in planets:
            planet.draw(window)

        pygame.display.update()

    pygame.quit()

main()
