import pygame
from resources import resource_path
import spritebase

class SimpleSprite(spritebase.SpriteBase):
    def __init__(self, pos, img):
        spritebase.SpriteBase.__init__(self, pos)
        if isinstance(img, str):
            self.image = pygame.image.load(resource_path(img)).convert_alpha()
        else:
            self.image = img
        self._width = 0
        self._height = 0
        if self.image:
            self._width = self.image.get_rect()[2]
            self._height = self.image.get_rect()[3]
        self._recalc_rect()