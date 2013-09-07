import sys
import pygame
import lifter
import gravity
import settings
import universals as UNI
#from data import filepath as FILES

class Level:
    def __init__(self, screen):
        self.screen = screen
        self._quit = False
        self.clock = pygame.time.Clock()
        self.gravity = gravity.Gravity(UNI.GRAVITY)
        self.playerGroup = pygame.sprite.Group()
        self.lifter = lifter.Lifter(self.playerGroup)

    def processEvents(self):
        pressed = pygame.key.get_pressed()
        print(pressed)
        print(pygame.K_ESCAPE)
        if pressed[pygame.K_ESCAPE]:
            self._quit = True
        if pressed[pygame.K_UP]:
            self.lifter.thrustUp()
        if pressed[pygame.K_LEFT]:
            self.lifter.thrustLeft()
        if pressed[pygame.K_RIGHT]:
            self.lifter.thrustRight()

        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

            """"
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self._quit = True
                if event.key == pygame.K_UP:
                    self.lifter.thrustUp()
                if event.key == pygame.K_DOWN:
                    print("K_DOWN")
                    """

    def update(self):
        self.gravity.affect(self.playerGroup)
        self.playerGroup.update()

    def draw(self):
        self.screen.fill(UNI.BACKGROUND)
        self.playerGroup.draw(self.screen)

    def run(self):
        while not self._quit:
            self.processEvents()
            self.update()
            self.draw()
            pygame.display.flip()
            self.clock.tick(settings.TICK_RATE)



