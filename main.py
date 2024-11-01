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
background_image=pg.image.load('ExternalArt\Free War Game Kit\Background\Background_1920x1080.png')
main_base=base.Base(0)
soldier=units.Soldier()
character_selected=False
selected_character=None
mouse_down=False
over_character=False
while running:
    events=pg.event.get()
    mouse_pos=pg.mouse.get_pos()
    for event in events:
        if event.type==pg.QUIT:
            running=False
        if event.type==pg.MOUSEBUTTONDOWN:
            if character_selected == False:
                for obj in main_base.inventory.active_units:
                    if obj.rect.collidepoint(mouse_pos) and obj.waiting:
                        print(obj,"is selected")
                        
                        character_selected=True
                        selected_character=obj
                        over_character=True
                    else:
                        over_character=False
                if over_character==False:
                    if main_base.inventory.unit_selected!='':
                        main_base.mouse_down=True
                    elif main_base.inventory.unit_selected=='':
                        main_base.inventory.mouse_down=True
            mouse_down=True        

    #print(main_base.inventory.mouse_down)
    screen.fill('black')
    screen.blit(background_image,pg.Vector2(0,0))
    main_base.user_input()
    # soldier.animator.play(soldier.current_animation)    
    # screen.blit(soldier.animator.load_frame(),pg.Vector2(0,0))
    if character_selected:
        mouse_down=command_given=base.command_selection(selected_character,screen,mouse_pos,mouse_down)  
        base.taking_command=True
        
        if command_given:
            selected_character.timer=60
            selected_character.waiting=False
            character_selected=False
            base.taking_command=mouse_down=False

          

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
        active_unit.turn_timer()
        screen.blit(active_unit.animator.load_frame(active_unit.flip),active_unit.position)
        active_unit.health_bar.load_bar(screen,active_unit.position,pg.Vector2(24,100))
        active_unit.animation_bar.load_bar(screen,active_unit.position,pg.Vector2(24,72))
        active_unit.update_values()

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
            if character_selected==False:
                over_slot=slot.unit_select(mouse_pos,screen,(slot_pos-2,-2))
                if over_slot and main_base.inventory.mouse_down:
                    main_base.inventory.mouse_down=False
                    main_base.inventory.unit_selected=slot.unit_name
               

    #print(main_base.inventory.unit_selected)
    
    pg.display.flip()
    dt=clock.tick(60)/1000