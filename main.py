import pygame as pg
import base
import animation
import units
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
soldier=units.Soldier()
character_selected=False
selected_character=None
mouse_down=False
while running:
    mouse_pos=pg.mouse.get_pos()
    for event in pg.event.get():
        if event.type==pg.QUIT:
            running=False
        if event.type==pg.MOUSEBUTTONDOWN:
            if character_selected == False:
                for obj in main_base.inventory.active_units:
                    if obj.rect.collidepoint(mouse_pos) and obj.waiting:
                        print(obj,"is selected")
                        
                        character_selected=True
                        selected_character=obj
            mouse_down=True        

    
    screen.fill('black')
    screen.blit(background_image,pg.Vector2(0,0))
    main_base.user_input()
    # soldier.animator.play(soldier.current_animation)    
    # screen.blit(soldier.animator.load_frame(),pg.Vector2(0,0))
    if character_selected:
        mouse_down=command_given=base.command_selection(selected_character,screen,mouse_pos,mouse_down)  
        if command_given:
            selected_character.timer=60
            selected_character.waiting=False
            character_selected=False
          

    #screen.blit(soldier_anim.load_frame(),pg.Vector2(width/2,height/2))
    #soldier_anim.play("walk")
    #if bool(main_base.inventory.inventory_open)==True:
        #main_base.inventory.inventory_opened()
    #pg.draw.rect(screen,'red',pg.Rect((0-camera.offset.x,0-camera.offset.y),(50,50)))
    #pg.draw.circle(screen,'red',pl.position-camera.offset,30)
    keys = pg.key.get_pressed()
    for active_unit in main_base.inventory.active_units:  
        active_unit.animator.play(active_unit.current_animation)
        active_unit.turn_timer()
        screen.blit(active_unit.animator.load_frame(),active_unit.position)
    pg.display.flip()
    dt=clock.tick(60)/1000