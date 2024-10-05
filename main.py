import pygame as pg
import base
"""Main python file which will run the gameloop.
   The Display is 1000px x 720px 60 frames persec"""
pg.init()
width=1200
height=676
screen=pg.display.set_mode((width,height),depth=1)
clock=pg.time.Clock()
running=True
dt=0
background_image=pg.image.load('D:\Games\CalmBeforeTheStorm\ExternalArt\Free War Game Kit\Background\Background_1920x1080.png')
main_base=base.Base(0)
while running:
    
    for event in pg.event.get():
        if event.type==pg.QUIT:
            running=False

    screen.fill('black')
    screen.blit(background_image,pg.Vector2(0,0))
    main_base.user_input()
    #if bool(main_base.inventory.inventory_open)==True:
        #main_base.inventory.inventory_opened()
    #pg.draw.rect(screen,'red',pg.Rect((0-camera.offset.x,0-camera.offset.y),(50,50)))
    #pg.draw.circle(screen,'red',pl.position-camera.offset,30)
    
    pg.display.flip()
    dt=clock.tick(60)/1000