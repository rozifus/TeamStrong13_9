import sys
import time
import random
import textwrap
import level

import pygame
from pygame.transform import scale2x, scale
from pygame.image import load

from data import filepath
import settings


def main():

    """ your app starts here
    """
    pygame.init()

    screen = pygame.display.set_mode(settings.DISPLAY_SIZE)

    while 1:
        level1 = level.Level(screen)
        level1.run()


