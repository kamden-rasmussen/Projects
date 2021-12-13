import pygame
import random


class Ball:

    def __init__(self, size, min_x, max_x, min_y, max_y, left_paddle_x, right_paddle_x):
        self._size = size
        # X's ---------------------------------------------
        self._minX = min_x
        self._maxX = max_x
        self._mX = self._minX
        self._mDX = 0
        # Y's --------------------------------------------
        self._minY = min_y
        self._maxY = max_y
        self._mY = min_y
        self._mDY = 0
        # Paddles -----------------------------------------
        # Left
        self._leftPaddleX = left_paddle_x
        self._mLeftPaddleMinY = min_y
        self._mLeftPaddleMaxY = max_y
        # Right
        self._rightPaddleX = right_paddle_x
        self._mRightPaddleMinY = min_y
        self._mRightPaddleMaxY = max_y

    def getX(self):
        return self._mX

    def getY(self):
        return self._mY

    def getSize(self):
        return self._size

    def getDX(self):
        return self._mDX

    def getDY(self):
        return self._mDY

    def getMinX(self):
        return self._minX

    def getMinY(self):
        return self._minY

    def getMaxX(self):
        return self._maxX

    def getMaxY(self):
        return self._maxY

    # Left Paddle -------------------------
    def getLeftPaddleX(self):
        return self._leftPaddleX

    def getLeftPaddleMinY(self):
        return self._mLeftPaddleMinY

    def getLeftPaddleMaxY(self):
        return self._mLeftPaddleMaxY

    # Right Paddle -------------------------------
    def getRightPaddleX(self):
        return self._rightPaddleX

    def getRightPaddleMinY(self):
        return self._mRightPaddleMinY

    def getRightPaddleMaxY(self):
        return self._mRightPaddleMaxY

    def setPosition(self, x, y):
        if (x + self._size) < self._maxX and x > self._minX:
            if (y + self._size) < self._maxY and y > self._minY:
                self._mX = x
                self._mY = y
        return

    def setSpeed(self, dx, dy):
        self._mDX = dx
        self._mDY = dy
        return

    def setLeftPaddleY(self, paddle_min_y, paddle_max_y):

        if self._maxY >= paddle_max_y > paddle_min_y >= self._minY:
            self._mLeftPaddleMaxY = paddle_max_y
            self._mLeftPaddleMinY = paddle_min_y
        return

    def setRightPaddleY(self, paddle_min_y, paddle_max_y):
        if self._maxY >= paddle_max_y > paddle_min_y >= self._minY:
            self._mRightPaddleMaxY = paddle_max_y
            self._mRightPaddleMinY = paddle_min_y

        return

    def checkTop(self, new_y):
        if new_y >= self._minY:
            return new_y
        else:
            disOut = self._minY - new_y
            new_y += 2 * disOut
            self._mDY *= -1
        return new_y

    def checkBottom(self, new_y):
        if (new_y + self._size) <= self._maxY:
            return new_y
        else:
            disOut = self._maxY - (new_y + self._size)
            new_y += (2 * disOut)
            self._mDY *= -1
        return new_y

    def checkLeft(self, new_x):
        if new_x > self._minX:
            return new_x
        else:
            self._mDX = 0
            self._mDY = 0
            disOut = self._minX - new_x
            new_x += disOut
            return new_x

    def checkRight(self, new_x):
        if (new_x + self._size) < self._maxX:
            return new_x
        else:
            self._mDX = 0
            self._mDY = 0
            new_x = self._maxX - self._size
            return new_x

    def checkLeftPaddle(self, new_x, new_y):
        midY = ((new_y + self._mY) / 2)
        if self._mX < self._leftPaddleX or new_x > self._leftPaddleX or self._mDX > 0:
            return new_x
        elif self._mLeftPaddleMaxY < new_y or self._mLeftPaddleMinY > new_y:
            return new_x
        elif self._mLeftPaddleMinY <= midY <= self._mLeftPaddleMaxY:
            disOut = self._leftPaddleX - new_x
            new_x += 2 * disOut
            self._mDX *= -1
            return new_x

    def checkRightPaddle(self, new_x, new_y):
        midY = ((new_y + self._mY) / 2)
        if self._mX > self._rightPaddleX or (new_x + self._size) < self._rightPaddleX or self._mDX < 0:
            return new_x
        elif self._mRightPaddleMaxY < new_y or self._mRightPaddleMinY > new_y:
            return new_x
        elif self._mRightPaddleMinY <= midY <= self._mRightPaddleMaxY:
            disOut = self._rightPaddleX - (new_x + self._size)
            new_x += 2 * disOut
            self._mDX *= -1
            return new_x



    def move(self, dt):
        new_x = (dt * self._mDX) + self._mX
        new_y = (dt * self._mDY) + self._mY
        new_y = self.checkTop(new_y)
        new_y = self.checkBottom(new_y)
        new_x = self.checkLeft(new_x)
        new_x = self.checkRight(new_x)
        new_x = self.checkLeftPaddle(new_x, new_y)
        new_x = self.checkRightPaddle(new_x, new_y)
        self._mX = new_x
        self._mY = new_y
        return

    def serveLeft(self, x, min_y, max_y, min_dx, max_dx, min_dy, max_dy):
        y = random.uniform(min_y, max_y)
        dx = random.uniform(min_dx, max_dx)
        dy = random.uniform(min_dy, max_dy)
        self._mX = x
        self._mY = y
        self._mDX = dx
        self._mDY = dy
        return

    def serveRight(self, x, min_y, max_y, min_dx, max_dx, min_dy, max_dy):
        y = random.uniform(min_y, max_y)
        dx = random.uniform(min_dx, max_dx)
        dy = random.uniform(min_dy, max_dy)
        self._mX = x
        self._mY = y
        self._mDX = -dx
        self._mDY = dy
        return

    def draw(self, surface):
        Rect = [self._mX, self._mY, self._size, self._size]
        pygame.draw.rect(surface, [255, 255, 255], Rect, 0)
        return
