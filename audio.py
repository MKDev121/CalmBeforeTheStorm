import pygame as pg

pg.mixer.init()
class AudioSource:

    def __init__(self,channel_index,sounds={}):
        self.channel_index=channel_index
        self.sounds=sounds
        self.channel=pg.mixer.Channel(channel_index)

    def play(self,name):
        self.channel.play(self.sounds[name])
    
    def add_sound(self,name,path):
        self.sounds[name]=pg.mixer.Sound(path)

