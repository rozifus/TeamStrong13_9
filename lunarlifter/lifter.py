import pygame
from pygame.transform import scale2x, scale, rotate
from pygame.image import load
import universals as UNI
from data import filepath

class Lifter(pygame.sprite.Sprite):

    def __init__(self, *groups):
        super(Lifter, self).__init__(*groups)
        #self._speed = 0
        self.image_base = scale2x(load(filepath('lifter.png'))).convert_alpha()
        self.image = self.image_base
        #self.mask = pygame.mask.from_surface(self.image)
        self.rect = pygame.Rect(
            (100,100), self.image.get_size())

        self._xspeed = 0
        self._yspeed = 0
        self._rotspeed = 0
        self._rotation = 0

        self._sounds = {
            'dead': pygame.mixer.Sound(filepath('buggy-hit.wav')),
            'jump': pygame.mixer.Sound(filepath('jump.wav'))}

    def reset(self):
        """
        The car has died, reset its state.
        """
        self._xspeed = 0
        self._yspeed = 0
        self._jumping = False
        self.rect.left = 100
        self.rect.bottom = self._groundy

    def thrustUp(self):
        self._yspeed += UNI.THRUST_UP

    def thrustLeft(self):
        self._rotspeed += UNI.THRUST_SIDE

    def thrustRight(self):
        self._rotspeed -= UNI.THRUST_SIDE

    """
    def change_speed(self, direction):
        self._xspeed += direction * settings.BUGGY_SPEED
        self._xspeed = max(self._xspeed, -settings.BUGGY_SPEED)
        self._xspeed = min(self._xspeed, settings.BUGGY_SPEED)

    def jump(self, force=settings.BUGGY_JUMP_FORCE):
        if not self._jumping:
            self._yspeed = -force
            self._jumping = True
            self._sounds['jump'].play()
    """

    def update(self):
        self.rect.move_ip(self._xspeed, -self._yspeed)
        oldCenter = self.rect.center
        self._rotation += self._rotspeed
        self.image = rotate(self.image_base, self._rotation)
        self.rect.center = oldCenter
