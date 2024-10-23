import pygame as pg

class Animator:
    def __init__(self,current_frame,dt):
        self.animations={}
        self.dt=dt
        self.animator_timer=0
        self.current_frame=current_frame+"_walk_2.png"
    def play(self,animation_name):
        if self.animator_timer>=0:
            self.animator_timer-=self.dt
        else:
            self.current_frame=self.animations[animation_name].return_frame()#frame location
            self.animator_timer=self.animations[animation_name].interval#interval
        
        
    def load_frame(self):
        return pg.image.load(self.current_frame)
class Animation:
    def __init__(self,frame_count,frame_location):
        self.frame_count=frame_count
        self.frame_location=frame_location
        self.interval=frame_count/10
        self.looping=True
        self.index=1
    def return_frame(self):
        if self.index<self.frame_count:
            self.index+=1
        else:
            if self.looping:
                self.index=1
        return self.frame_location+str(self.index)+".png"
