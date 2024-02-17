import math
import pygame.draw

WIDTH, HEIGHT = 800, 800

class Planet:
    AU = 149.6E6 * 1000    # ASTRONOMICAL UNIT : DISTANCE B/W SUN AND EARTH
    G = 6.67428e-11         # GRAVITATIONAL CONSTANT
    SCALE = 250 / AU
    TIMESTEP = 3600 * 24    # 1 DAY IN SECONDS

    def __init__(self, x, y, radius, color, mass):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.mass = mass

        self.orbit = []
        self.sun = False
        self.distance_to_sun = 0

        self.x_vel = 0
        self.y_vel = 0

    def draw(self, win):
        x = self.x * self.SCALE + WIDTH/2
        y = self.y * self.SCALE + HEIGHT/2
        pygame.draw.circle(win, self.color,(x, y), self.radius)
