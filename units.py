"""A script containing all classes of units"""
import pygame as pg
import animation
"""Base class unit"""
class Unit:
    def __init__(self,health,price,name,frame_location):
        self.name=name
        self.health=health
        self.price=price
        self.position=pg.Vector2(0,0)
        self.frame_location=frame_location
        self.animator=animation.Animator()
        
class Soldier(Unit):
    def __init__(self,health=100,price=10,name='soldier') -> None:
        super().__init__(health,price,name)

class Turret(Unit):
    def __init__(self,health=200,price=100,name='turret') -> None:
        super().__init__(health,price,name)

class Tank(Unit):
    def __init__(self,health=200,price=200,name='tank') -> None:
        super().__init__(health,price,name)
class Airplane(Unit):
    def __init__(self,price=500,name='airplane') -> None:
        super().__init__(price,name)