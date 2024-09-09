import pygame as pg
import objects
"""Main python file which will run the gameloop.
   The Display is 1000px x 720px 60 frames persec"""
pg.init()
screen=pg.display.set_mode((1200,676),depth=1)
clock=pg.time.Clock()
running=True
dt=0
background=objects.Background(pg.Vector2(0,0),pg.image.load(r'D:\Games\CalmBeforeTheStorm\ExternalArt\Free War Game Kit\Background\Background_1920x1080.png'))

speed=400
while running:
    
    for event in pg.event.get():
        if event.type==pg.QUIT:
            running=False

    screen.fill('black')
    
    #pg.draw.rect(screen,'red',pg.Rect((0-camera.offset.x,0-camera.offset.y),(50,50)))
    screen.blit(background.image,background.position)
    #pg.draw.circle(screen,'red',pl.position-camera.offset,30)
    keys =pg.key.get_pressed()
    pg.display.flip()
    dt=clock.tick(60)/1000