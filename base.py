"""A script containing base class and inventory class"""
import pygame as pg
import keyboard 
import units as uni
import pygame_widgets as pw
units={'soldier':0,
       'turrets':0,
       'tank':0,
       'airplane':0}
shop={'soldier':10,
      'turret':100,
      'tank':200,
      'airplane':500}

target_keys=[pg.K_i,pg.K_s]
taking_command=False
class Base:
    """Object which is the main control unit in the game, which we have to defend from enemies"""
    def __init__(self,position):
        self.position=position
        self.inventory=Inventory() 
        self.health=100
        self.keysdown=False
        self.active_key=None
        self.mouse_down=False
        
        
    def user_input(self):
        """Keeps track of all the user input and responds with corresponding action"""
        keys=pg.key.get_pressed()
        self.mouse_pos=pg.mouse.get_pos()
        if self.keysdown==False :
            if keys[pg.K_i]:
                self.inventory.inventory_open=~self.inventory.inventory_open
                print('Inventory Open:',self.inventory.inventory_open)
                    
                self.active_key=pg.K_i
                self.keysdown=True
            elif keys[pg.K_a]:
                print('Attack!')
                self.active_key=pg.K_a
                self.keysdown=True
            
            #Spawning units
            if bool(self.inventory.inventory_open)==True and self.mouse_down:
                if self.inventory.unit_selected=="soldier" :#Spawn soldier
                    print('Soldier Spawned')
                    self.active_key=pg.K_1
                    self.inventory.unit_spawning(uni.Soldier(position=pg.Vector2(self.mouse_pos[0],540)))
                    self.keysdown=True
                elif self.inventory.unit_selected=="turret":#Spawn turret
                    print('Turret Spawned')
                    self.active_key=pg.K_2
                    self.inventory.unit_spawning(uni.Turret(position=pg.Vector2(self.mouse_pos[0],515)))
                    self.keysdown=True
                elif self.inventory.unit_selected=="tank":#Spawn tank
                    print('Tank spawned')
                    self.active_key=pg.K_3
                    self.inventory.unit_spawning(uni.Tank(position=pg.Vector2(self.mouse_pos[0],500)))
                    self.keysdown=True
                elif self.inventory.unit_selected=="airplane":#Spawn plane
                    print('Plane spawned')
                    self.inventory.unit_spawning(uni.Airplane(position=pg.Vector2(self.mouse_pos[0],10)))
                    
                    self.active_key=pg.K_4
                    self.keysdown=True
                self.inventory.unit_selected=''
                self.mouse_down=False
                
        if self.active_key!=None:
            self.keysdown=keys[self.active_key]
        
            
    def key_down(self,key,is_keydown):
        if key:
            is_keydown=True
            return True
        else:
            return False
        key=is_keydown                                       
            
class Key:       
    def __init__(self,keydown_state=0):
        self.keydown_state=keydown_state    


class Inventory:
    """Subclass of base, which keeps track of all the units both passive and active. Also manages the shop system"""

    def __init__(self):
        self.units=units
        self.shop=shop
        self.inventory_open=False
        self.active_units=[]
        self.economy=1000
        self.intial_slot_pos=pg.Vector2(460,0)
        self.slots=[InventorySlot("soldier"),InventorySlot("turret"),InventorySlot("tank",(5,5)),InventorySlot("airplane",(5,0))]
        self.unit_selected=''
        self.mouse_down=False
    
    def inventory_opened(self):
        """The function which will display the UI icons of units and manages all the commands of inventory when it is opened"""
        print('The units are:')
        for unit_name in self.units:
            print(unit_name,end=' ')
        print()
    def unit_spawning(self,unit):
        """The function which will do the spawning of units from inventory to battleground"""
        self.units[unit.name]-=1
        self.active_units.append(unit)
        print(self.active_units)
            
        print('player is spawning something')
    
    def buying_units(self):
        """The function which will manage buying of units and store them in inventory"""
        
        print('player is buying something')
class InventorySlot:
    def __init__(self,unit_name,image_offset=(0,0),scale=70):
        self.unit_name=unit_name
        self.slot_image=pg.transform.smoothscale(pg.image.load(r'ArtByMe\Inventory_Slot.png'),(scale,scale))
        self.slot_item_image=pg.transform.smoothscale(pg.image.load(r"ExternalArt\Free War Game Kit\InventoryIcon\_"  +self.unit_name+".png"),(65,65))
        self.image_offset=image_offset
        self.rect=pg.Rect(((0,0)),(self.slot_image.get_width(),self.slot_image.get_height()))
    def unit_select(self,mouse_pos,screen,pos):
        
        if self.rect.collidepoint(mouse_pos) :
            pg.draw.rect(screen,(255,255,255),(pos,(75,75)),width=5)
        return self.rect.collidepoint(mouse_pos)



    
class Text:
    def __init__(self,font,text,pos):
        self.font=font
        self.text=text
        self.pos=pos
        self.text_surf=font.render(self.text,True,"white") 
        self.rect=pg.Rect(self.pos,(120,30))
       
def command_selection(obj,screen,mouse_pos,mouse_down):
    moves= list(obj.animator.animations.keys())
    
    max_len=0
    font =pg.font.Font(size=36)
    moves_text=[]
    for move in moves:
        ele=Text(font,move,(obj.position.x+20,obj.position.y-obj.img.get_height()+moves.index(move)*50+10))
        if max_len < ele.text_surf.get_width():
            max_len=ele.text_surf.get_width()
        moves_text.append(ele)       
    pg.draw.rect(screen,(58,58,58),((obj.position.x,obj.position.y-obj.img.get_height()),(max_len+30,50*len(moves))))
    pg.draw.rect(screen,(152,152,152),((obj.position.x,obj.position.y-obj.img.get_height()),(max_len+30,50*len(moves))),width=5)
    for move_text in moves_text:
        screen.blit(move_text.text_surf,move_text.pos)
        if move_text.rect.collidepoint(mouse_pos):
            if mouse_down: 
                obj.current_animation=move_text.text
                print('command selected')
                return True        



    