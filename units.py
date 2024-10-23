"""A script containing all classes of units"""
import pygame as pg
import animation
"""Base class unit"""
art_loc='D:\Games\CalmBeforeTheStorm\ExternalArt\Free War Game Kit\Characters'
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
        
    def load_obj(self,screen):
        screen.blit(self.animator.play(self.current_animation),pg.Vector2(0,0))
        
        
class Soldier(Unit):
    def __init__(self,health=100,price=10,name='soldier',frame_location=art_loc+r"\Soldier\PNG\Soldier_2",dt=0.14,position=pg.Vector2(0,0)) -> None:
        super().__init__(health,price,name,frame_location,dt,position)
        self.animator.animations["walk"]=animation.Animation(8,self.frame_location+"_walk_")
        self.animator.animations["shot_front"]=animation.Animation(8,self.frame_location+"_shot_front_")
    
    

class Turret(Unit):
    def __init__(self,health=200,price=100,name='turrets',frame_location=art_loc+r"\Turret\PNG\turret_1",dt=0.14,position=pg.Vector2(0,0)) -> None:
        super().__init__(health,price,name,frame_location,dt,position)


class Tank(Unit):
    def __init__(self,health=200,price=200,name='tank',frame_location=art_loc+r"\Tank\PNG\American_sherman",dt=0.14,position=pg.Vector2(0,0)) -> None:
        super().__init__(health,price,name,frame_location,dt,position)
class Airplane(Unit):
    def __init__(self,price=500,name='airplane',frame_location=art_loc+r"\Airplanes\Fokker\Skin 1\PNG\Fokker",dt=0.14,position=pg.Vector2(0,0)) -> None:
        super().__init__(1000,price,name,frame_location,dt,position)