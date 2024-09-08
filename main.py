import pygame as pg
"""Main python file which will run the gameloop.
   The Display is 1000px x 720px 60 frames persec"""
pg.init()
screen=pg.display.set_mode((1000,720))
clock=pg.time.Clock()
running=True
dt=0

while running:
    for event in pg.event.get():
        if event.type==pg.QUIT:
            running=False
    
    screen.fill('purple')
    pg.display.flip()
    dt=clock.tick(60)/1000