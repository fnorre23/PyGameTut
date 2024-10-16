import pygame as pg
from os.path import join
import random

# general setup
pg.init()
window_w, window_h = 1280, 720
display_surface = pg.display.set_mode((window_w, window_h))
# Setting window title
pg.display.set_caption('Space shooter video game')

running = True

# plain surface
surface = pg.Surface((100,200))
surface.fill('orange')
x = 100

# importing an image
player_surface = pg.image.load(join('..', 'images', 'player.png')).convert_alpha()
star_surface = pg.image.load(join('..', 'images', 'star.png')).convert_alpha()
star_positions = [(random.randint(0, window_w),(random.randint(0, window_h))) for i in range(20)]

while running:
    # event loop
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    x += 1

    # draw the game
    display_surface.fill('darkgrey')
    display_surface.blit(player_surface, (x,150))
    
    for pos in star_positions:
        display_surface.blit(star_surface, pos)

    pg.display.update()

pg.quit()