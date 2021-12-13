import pygame
from pong_starter import text


class ScoreBoard:

    def __init__(self, x, y, width, height):

        self._x = x
        self._y = y
        self._width = width
        self._height = height
        self._mLeftScore = 0
        self._mRightScore = 0
        self._mServerStatus = 1

        return

    def getX(self):
        return self._x

    def getY(self):
        return self._y

    def getWidth(self):
        return self._width

    def getHeight(self):
        return self._height

    def getLeftScore(self):
        return self._mLeftScore

    def getRightScore(self):
        return self._mRightScore

    def getServeStatus(self):
        return self._mServerStatus

    def isGameOver(self):
        r = False
        if self._mServerStatus == 3:
            r = True
        elif self._mServerStatus == 4:
            r = True
        return r

    def scoreLeft(self):
        if self._mLeftScore < 9 and not self.isGameOver():
            self._mLeftScore += 1
            if self._mLeftScore >= 9 and self._mServerStatus < 3:
                self._mServerStatus = 3

        return

    def scoreRight(self):
        if self._mRightScore < 9 and not self.isGameOver():
            self._mRightScore += 1
            if self._mRightScore >= 9 and self._mServerStatus < 3:
                self._mServerStatus = 4

        return

    def swapServe(self):
        if self._mServerStatus == 1:
            self._mServerStatus = 2
        elif self._mServerStatus == 2:
            self._mServerStatus = 1
        return

    def draw(self, surface):
        lScore = text.Text(str(self._mLeftScore), self._x+25, self._y+20)
        rScore = text.Text(str(self._mRightScore), self._x+50, self._y+20)
        lScore.setColor([0, 0, 204])
        rScore.setColor([255, 0, 0])

        rect = [self._x, self._y, self._width, self._height]
        pygame.draw.rect(surface, [255, 255, 255], rect, 0)
        lScore.draw(surface)
        rScore.draw(surface)

        return
