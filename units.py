"""A script containing all classes of units"""
import pygame as pg
import animation
import shared
import base
from random import randint
"""Base class unit"""
art_loc='ExternalArt\Free War Game Kit\Characters'
def move_forward(position,move_speed,dir,dt):
    return position+pg.Vector2(move_speed*dt,0)*dir
def hor_shoot(position,range,is_enemy):
    
    ray=pg.Vector2(position.x+range,position.y)
    for object in shared.GameObjects:
        offset= object.position.x-position.x
        if abs(offset)<abs(range) and object.is_enemy!=is_enemy and abs(range)/range==abs(offset)/offset:
            return object
class Unit:
    def __init__(self,health,price,name,frame_location,dt,position=pg.Vector2(0,0)):
        self.name=name
        self.health=health
        self.price=price
        self.position=position
        self.frame_location=frame_location
        self.dt=dt
        self.animator=animation.Animator(frame_location,dt)
        self.current_animation="default"
        self.animator.animations["default"]=animation.Animation(1,frame_location+"_default_")
        self.img=pg.image.load(self.animator.current_frame)
        self.rect=pg.Rect((self.position,(self.img.get_width(),self.img.get_height())))
        self.timer=0
        self.waiting=False
        self.flip=False
        self.taking_command=False
        self.health_bar=Bar(self.health,r"ArtByMe\Bar_Slot.png",100,pg.Vector2(0,-20))
        self.animation_bar=Bar(self.timer,r"ArtByMe\Bar_Slot.png",60,pg.Vector2(0,0),(0,0,255))
        self.mouse_down=False
        self.mouse_pos=pg.mouse.get_pos()
        self.command_given=False
        self.is_enemy=False
        self.enemy_moves=list(self.animator.animations.keys())
        
    def update_values(self):
        #screen.blit(self.animator.play(self.current_animation),pg.Vector2(0,0))
        dir=1
        self.health_bar.value=self.health
        if not(self.is_enemy):
            self.animation_bar.value=self.timer
            
            if self.rect.collidepoint(shared.mouse_pos):
                if shared.mouse_down and shared.mouse_current_state=='free' and self.waiting:
                    shared.mouse_current_state=shared.mouse_states[0]
                    shared.selected_character=self
                    shared.player_audio_source.play('hover')
                    print("Hello")
            if shared.mouse_current_state=='character_selected' and shared.selected_character==self:
                self.command_given=base.command_selection(self,shared.screen,shared.mouse_pos,shared.mouse_down)
            if self.command_given:
                self.timer=60
                self.waiting=False
                self.command_given=False
                shared.selected_character=None
            dir=-1
        else:
            self.enemy_moves=list(self.animator.animations.keys())
            dir=1

        if self.name=='soldier':
            if self.current_animation=="walk":
                self.position=move_forward(self.position,1,dir,self.dt)
            elif self.current_animation=="shot_front" and self.animator.animations[self.current_animation].index==4:
                obj=hor_shoot(self.position,400*dir,self.is_enemy)
                if obj!=None and (obj.name=='soldier' or obj.name=='tank' or obj.name=='turret'):
                    obj.health-=.5
        if self.name=='tank':
            if self.current_animation=="move_forward":
                self.position=move_forward(self.position,.5,dir,self.dt)
            elif self.current_animation=="attack" and self.animator.animations[self.current_animation].index==2:
                obj=hor_shoot(self.position,800*dir,self.is_enemy)
                if obj!=None and (obj.name=='soldier' or obj.name=='tank' or obj.name=='turrets'):
                    obj.health-=2
    

            
            

    def turn_timer(self):
        if self.timer>=0:
            self.timer-=self.dt
        else:
            if self.is_enemy:
                
                self.current_animation=self.enemy_moves[randint(0,len(self.enemy_moves)-1)]
                self.timer=30
            else:

                self.current_animation="default"
                self.waiting=True
        
        
class Soldier(Unit):
    def __init__(self,health=100,price=10,name='soldier',frame_location=art_loc+r"\Soldier\PNG\Soldier_2",dt=0.14,position=pg.Vector2(0,0)) -> None:
        super().__init__(health,price,name,frame_location,dt,position)
        self.animator.animations["walk"]=animation.Animation(8,self.frame_location+"_walk_")
        self.animator.animations["shot_front"]=animation.Animation(8,self.frame_location+"_shot_front_")
        self.move_speed=1
    
        
    
    

class Turret(Unit):
    def __init__(self,health=200,price=100,name='turrets',frame_location=art_loc+r"\Turret\PNG\turret_1",dt=0.14,position=pg.Vector2(0,0)) -> None:
        super().__init__(health,price,name,frame_location,dt,position)
        self.animator.animations["fire"]=animation.Animation(8,self.frame_location+"_fire_")
        self.health_bar=Bar(self.health,r"ArtByMe\Bar_Slot.png",200,pg.Vector2(60,-30))
        self.animation_bar=Bar(self.timer,r"ArtByMe\Bar_Slot.png",60,pg.Vector2(60,-10),(0,0,255))
        


class Tank(Unit):
    def __init__(self,health=200,price=200,name='tank',frame_location=art_loc+r"\Tank\PNG\American_sherman",dt=0.14,position=pg.Vector2(0,0)) -> None:
        super().__init__(health,price,name,frame_location,dt,position)
        self.animator.animations["attack"]=animation.Animation(8,self.frame_location+"_attack_")
        self.animator.animations["move_forward"]=animation.Animation(8,self.frame_location+"_move_forward_")
        self.flip=True
        self.health_bar=Bar(self.health,r"ArtByMe\Bar_Slot.png",200,pg.Vector2(100,10))
        self.animation_bar=Bar(self.timer,r"ArtByMe\Bar_Slot.png",60,pg.Vector2(100,30),(0,0,255))
        
class Airplane(Unit):
    def __init__(self,price=500,name='airplane',frame_location=art_loc+r"\Airplanes\Fokker\Skin 1\PNG\Fokker",dt=0.14,position=pg.Vector2(0,0)) -> None:
        super().__init__(1000,price,name,frame_location,dt,position)
        self.flip=True
class Bar:
    def __init__(self,value,bar,max_value,offset=pg.Vector2(0,0),color=(0,255,0)):
        self.value=value
        self.bar=bar
        self.position_offset=pg.Vector2(0,0)
        self.max_value=max_value
        self.offset=offset
        self.color=color
        
    def load_bar(self,screen,position,size):
        bar_img=pg.transform.smoothscale(pg.image.load(self.bar),size)
        real_size=((self.value/self.max_value)*size.x,size.y)
        pivot_correction=size.y-real_size[1]
        pg.draw.rect(screen,self.color,(position+pg.Vector2(self.offset.x+5,self.offset.y+pivot_correction),real_size-pg.Vector2(5,5)))
        screen.blit(bar_img,position+self.offset)


        