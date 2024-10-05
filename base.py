"""A script containing base class and inventory class"""
import pygame as pg
import keyboard 
import units as uni
units={'soldier':0,
       'turrets':0,
       'tanks':0,
       'planes':0}
shop={'soldier':10,
      'turret':100,
      'tank':200,
      'airplane':500}

target_keys=[pg.K_i,pg.K_s]

class Base:
    """Object which is the main control unit in the game, which we have to defend from enemies"""
    def __init__(self,position):
        self.position=position
        self.inventory=Inventory() 
        self.health=100
        self.keysdown=False
        self.active_key=None
        
    def user_input(self):
        """Keeps track of all the user input and responds with corresponding action"""
        keys=pg.key.get_pressed()
        
        if self.keysdown==False:
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
            if bool(self.inventory.inventory_open)==True:
                if keys[pg.K_1]:#Spawn soldier
                    print('Soldier Spawned')
                    self.active_key=pg.K_1
                    self.inventory.unit_spawning(uni.Soldier())
                    self.keysdown=True
                elif keys[pg.K_2]:#Spawn turret
                    print('Turret Spawned')
                    self.active_key=pg.K_2
                    self.keysdown=True
                elif keys[pg.K_3]:#Spawn tank
                    print('Tank spawned')
                    self.active_key=pg.K_3
                    self.keysdown=True
                elif keys[pg.K_4]:#Spawn plane
                    print('Plane spawned')
                    self.active_key=pg.K_4
                    self.keysdown=True
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