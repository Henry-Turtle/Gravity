import numpy
import pygame


class solarObject:
    def __init__(self, mass, pos, velocity, radius):
        self.mass = mass
        self.x, self.y = pos
        self.vx, self.vy = velocity
        self.radius = radius


pygame.init()
width, height = 700, 700
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
FPS = 60

WHITE = pygame.Color(255, 255, 255)
BLACK = pygame.Color(0, 0, 0)

solar_system = []
solar_system.append(solarObject(100, (width/2, height/2), (0, 0), 100)) #The Sun
solar_system.append(solarObject(1, (150, 150), (1, 2), 10)) #The earth

screen.fill(WHITE)

def draw_objects(screen, solar_objects):
    screen.fill(WHITE)
    for obj in solar_objects:
       pygame.draw.circle(screen, BLACK, (obj.x, obj.y), obj.radius)

def move_objects(screen, solar_objects):
    for obj in solar_objects:
        obj.x += obj.vx
        obj.y += obj.vy

while True:
    clock.tick(FPS)
    move_objects(screen, solar_system)
    draw_objects(screen, solar_system)
    
    

    pygame.display.flip()


    