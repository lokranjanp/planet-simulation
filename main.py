import pygame
from planets import Planet
from constants import *
pygame.init()

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Planet Simulation")

def main():
    run = True
    clock = pygame.time.Clock()

    sun = Planet(0, 0, 30, sun_color, mass_sun)
    sun.sun = True

    mercury = Planet(0.387 * AU, 0, 8, mercury_color, mass_mercury)
    mercury.sun = False

    venus = Planet(0.723 * AU, 0, 14, venus_color, mass_mercury)
    venus.sun = False

    earth = Planet(-1 * AU, 0, 16, earth_color, mass_earth)
    earth.sun = False

    mars = Planet(-1.524 * AU, 0, 12, mars_color, mass_mars)
    mars.sun = False

    earth.y_vel = earth_y_vel
    mars.y_vel = mars_y_vel
    venus.y_vel = venus_y_vel
    mercury.y_vel = mercury_y_vel

    planets = [sun, earth, mars, venus, mercury]

    while run:
        clock.tick(60)
        window.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        for planet in planets:
            planet.position_update(planets)
            planet.draw(window)

        pygame.display.update()

    pygame.quit()

main()
