import pygame


class Paddle:

    def __init__(self, x, y, width, height, speed, min_y, max_y):
        self._mX = x
        self._mY = y
        self._mWidth = width
        self._mHeight = height
        self._mSpeed = speed
        self._minY = min_y
        self._maxY = max_y

    def getX(self):
        return self._mX

    def getY(self):
        return self._mY

    def getWidth(self):
        return self._mWidth

    def getHeight(self):
        return self._mHeight

    def getSpeed(self):
        return self._mSpeed

    def getMinY(self):
        return self._minY

    def getMaxY(self):
        return self._maxY

    def getRightX(self):
        return self._mX + self._mWidth

    def getBottomY(self):
        return self._mY + self._mHeight

    def setPosition(self, y):

        if self._maxY >= (y + self.getHeight()) and y >= self._minY:
            self._mY = y
        else:
            self._mY = self._mY
        return

    def moveUp(self, dt):
        newY = self._mY - (dt * self._mSpeed)

        if newY >= self._minY:
            self._mY = self._mY - (dt * self._mSpeed)
        else:
            self._mY = self._minY
        return

    def moveDown(self, dt):
        newY = self._mY + (dt * self._mSpeed) + self._mHeight

        if newY <= self._maxY:
            self._mY = self._mY + (dt * self._mSpeed)
        else:
            self._mY = self._maxY - self._mHeight
        return

    def draw(self, surface):
        rect = [self._mX, self._mY, self._mWidth, self._mHeight]
        pygame.draw.rect(surface, [255, 255, 255], rect, 0)
        return
