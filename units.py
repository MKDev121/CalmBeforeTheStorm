"""A script containing all classes of units"""
import pygame as pg
import animation
"""Base class unit"""
art_loc='ExternalArt\Free War Game Kit\Characters'
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
        self.timer=60
        self.waiting=False
        self.flip=False
        self.taking_command=False
        self.health_bar=Bar(self.health,r"ArtByMe\Bar_Slot.png",100,pg.Vector2(self.img.get_width(),30))
        self.animation_bar=Bar(self.timer,r"ArtByMe\Bar_Slot.png",60,pg.Vector2(self.img.get_width()+21,57),(0,0,255))
        
        
    def update_values(self):
        #screen.blit(self.animator.play(self.current_animation),pg.Vector2(0,0))
        self.animation_bar.value=self.timer
    def turn_timer(self):
        if self.timer>=0:
            self.timer-=self.dt
        else:
            self.current_animation="default"
            self.waiting=True
        
        
class Soldier(Unit):
    def __init__(self,health=50,price=10,name='soldier',frame_location=art_loc+r"\Soldier\PNG\Soldier_2",dt=0.14,position=pg.Vector2(0,0)) -> None:
        super().__init__(health,price,name,frame_location,dt,position)
        self.animator.animations["walk"]=animation.Animation(8,self.frame_location+"_walk_")
        self.animator.animations["shot_front"]=animation.Animation(8,self.frame_location+"_shot_front_")
    
    

class Turret(Unit):
    def __init__(self,health=200,price=100,name='turrets',frame_location=art_loc+r"\Turret\PNG\turret_1",dt=0.14,position=pg.Vector2(0,0)) -> None:
        super().__init__(health,price,name,frame_location,dt,position)
        self.animator.animations["fire"]=animation.Animation(8,self.frame_location+"_fire_")
        self.health_bar=Bar(self.health,r"ArtByMe\Bar_Slot.png",200,pg.Vector2(self.img.get_width(),50))
        


class Tank(Unit):
    def __init__(self,health=200,price=200,name='tank',frame_location=art_loc+r"\Tank\PNG\American_sherman",dt=0.14,position=pg.Vector2(0,0)) -> None:
        super().__init__(health,price,name,frame_location,dt,position)
        self.animator.animations["attack"]=animation.Animation(8,self.frame_location+"_attack_")
        self.animator.animations["move_forward"]=animation.Animation(8,self.frame_location+"_move_forward_")
        self.flip=True
        self.health_bar=Bar(self.health,r"ArtByMe\Bar_Slot.png",200,pg.Vector2(self.img.get_width(),70))
        
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
        real_size=(size.x,(self.value/self.max_value)*size.y)
        pivot_correction=size.y-real_size[1]
        pg.draw.rect(screen,self.color,(position+pg.Vector2(self.offset.x+5,self.offset.y+pivot_correction),real_size-pg.Vector2(5,5)))
        screen.blit(bar_img,position+self.offset)


        