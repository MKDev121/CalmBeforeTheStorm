import pygame as pg
import base
import animation
import units
import shared
"""Main python file which will run the gameloop.
   The Display is 1000px x 720px 60 frames persec"""
pg.init()
width=1200
height=676
shared.screen=screen=pg.display.set_mode((width,height),depth=1)
clock=pg.time.Clock()
running=True
dt=0
background_image=pg.image.load('ExternalArt\Free War Game Kit\Background\Background_1920x1080.png')
main_base=base.Base(0)
soldier=units.Soldier()
character_selected=False
selected_character=None
mouse_down=False
over_character=False

while running:
    events=pg.event.get()
    mouse_pos=shared.mouse_pos=pg.mouse.get_pos()
    for event in events:
        if event.type==pg.QUIT:
            running=False
        if event.type==pg.MOUSEBUTTONDOWN:
            mouse_down=shared.mouse_down=True        

    #print(main_base.inventory.mouse_down)
    screen.fill('black')
    screen.blit(background_image,pg.Vector2(0,0))
    main_base.user_input()
    # soldier.animator.play(soldier.current_animation)    
    # screen.blit(soldier.animator.load_frame(),pg.Vector2(0,0))
    #screen.blit(soldier_anim.load_frame(),pg.Vector2(width/2,height/2))
    #soldier_anim.play("walk")
    #if bool(main_base.inventory.inventory_open)==True:
        #main_base.inventory.inventory_opened()
    #pg.draw.rect(screen,'red',pg.Rect((0-camera.offset.x,0-camera.offset.y),(50,50)))
    #pg.draw.circle(screen,'red',pl.position-camera.offset,30)
    keys = pg.key.get_pressed()

    #Loading and Displaying animation frames of active units
    for active_unit in main_base.inventory.active_units:  
        active_unit.animator.play(active_unit.current_animation)
        screen.blit(active_unit.animator.load_frame(active_unit.flip),active_unit.position)
        active_unit.health_bar.load_bar(screen,active_unit.position,pg.Vector2(100,24))
        active_unit.animation_bar.load_bar(screen,active_unit.position,pg.Vector2(72,24))
        active_unit.update_values()
        active_unit.turn_timer()

    #Loading and Displaying Game UI
 


    if bool(main_base.inventory.inventory_open) :
        slot_pos_count=0
        for slot in main_base.inventory.slots:
            slot_pos=main_base.inventory.intial_slot_pos.x + 75*slot_pos_count
            screen.blit(slot.slot_image,pg.Vector2(slot_pos,0))
            screen.blit(slot.slot_item_image,pg.Vector2(slot_pos+slot.image_offset[0],slot.image_offset[1]))
            slot.rect.x=slot_pos
            slot.rect.y=0
            slot_pos_count+=1
            if shared.mouse_current_state=='free':
                over_slot=slot.unit_select(shared.mouse_pos,screen,(slot_pos-2,-2))
                if over_slot and shared.mouse_down:
                    main_base.inventory.unit_selected=slot.unit_name
                    shared.mouse_current_state='spawning'
                    
               

    #print(main_base.inventory.unit_selected)
    
    pg.display.flip()
    if shared.mouse_current_state=='buffer':
        shared.mouse_current_state='free'
    if shared.mouse_down:
        shared.mouse_down=False
    dt=clock.tick(60)/1000
    