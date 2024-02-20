background_color = (255, 255, 255)      #WHITE
WIDTH, HEIGHT = 800, 800
AU = 149.6e6 * 1000  # ASTRONOMICAL UNIT : DISTANCE B/W SUN AND EARTH
G = 6.67428e-11  # GRAVITATIONAL CONSTANT
SCALE = 250 / AU
TIMESTEP = 3600 * 24  # 1 DAY IN SECONDS

mass_sun = 1.98892 * 10**30
mass_earth = 5.9742 * 10**24
mass_mars = 6.39 * 10**23
mass_mercury = 3.30 * 10**23
mass_venus = 4.8685 * 10**24

sun_color = (255, 255, 0)
earth_color = (100, 149, 237)
mars_color = (188, 39, 50)
mercury_color = (80, 78, 81)
venus_color = (255, 255, 255)

earth_y_vel = 29.783 * 1000
mars_y_vel = 24.077 * 1000
mercury_y_vel = 47.4 * 1000
venus_y_vel = -35.02 * 1000
