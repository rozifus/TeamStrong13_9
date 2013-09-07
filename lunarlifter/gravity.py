import sys
import pygame
import lifter
import settings
#import universals as UNI
#from data import filepath as FILES

class Gravity:
    def __init__(self, accel):
        self.accel = accel

    def affect(self, group):
        for entity in group:
            entity._yspeed += self.accel






