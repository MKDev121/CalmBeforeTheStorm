import pygame as pg
"""The  scripts which contains the  class of all game objects"""
class Base:
    def __init__(self,position,image):
        self.position=position
        self.intial_position=pg.Vector2(500,360)
        self.image=image
class Camera:
    def __init__(self,player_position):
        self.player_position=player_position
        #self.position=player_position
        self.offset=pg.Vector2(0,0)
class Background:
    def __init__(self,position,image):
        self.position=position
        self.image=image
