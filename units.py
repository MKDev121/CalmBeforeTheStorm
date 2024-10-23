"""A script containing all classes of units"""
import pygame as pg
import animation
"""Base class unit"""
class Unit:
    def __init__(self,health,price,name,frame_location,dt):
        self.name=name
        self.health=health
        self.price=price
        self.position=pg.Vector2(0,0)
        self.frame_location=frame_location
        self.dt=dt
        self.animator=animation.Animator(frame_location,dt)
        self.current_animation="default"
        
        
    def load_obj(self,screen):
        screen.blit(self.animator.play(self.current_animation),pg.Vector2(0,0))
        
        
class Soldier(Unit):
    def __init__(self,health=100,price=10,name='soldier',frame_location="D:\Games\CalmBeforeTheStorm\ExternalArt\Free War Game Kit\Characters\Soldier\PNG\Soldier_2",dt=0.14) -> None:
        super().__init__(health,price,name,frame_location,dt)
        self.animator.animations["default"]=animation.Animation(1,frame_location+"_default_")
        self.current_animation="default"
        self.animator.animations["walk"]=animation.Animation(8,self.frame_location+"_walk_")
        
    

class Turret(Unit):
    def __init__(self,health=200,price=100,name='turret') -> None:
        super().__init__(health,price,name)

class Tank(Unit):
    def __init__(self,health=200,price=200,name='tank') -> None:
        super().__init__(health,price,name)
class Airplane(Unit):
    def __init__(self,price=500,name='airplane') -> None:
        super().__init__(price,name)