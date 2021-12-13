import pygame


class Wall:

    def __init__(self, x, y, width, height):
        self._x = x
        self._y = y
        self._width = width
        self._height = height
        return

    def getX(self):
        return self._x

    def getY(self):
        return self._y

    def getWidth(self):
        return self._width

    def getHeight(self):
        return self._height

    def getRightX(self):
        return self._x + self._width

    def getBottomY(self):
        return self._y + self._height

    def draw(self, surface):
        color = [0, 204, 0]
        rect = [self._x, self._y, self._width, self._height]
        pygame.draw.rect(surface, color, rect, 0)

        return
