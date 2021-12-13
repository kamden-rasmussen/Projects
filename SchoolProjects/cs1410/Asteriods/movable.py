import math

class Movable:

    def __init__(self, mX, mY, mDx, mDy, mWorldWidth, mWorldHeight):
        self.mX = mX
        self.mY = mY
        self.mWorldWidth = mWorldWidth
        self.mWorldHeight = mWorldHeight
        self.mDx = mDx
        self.mDy = mDy
        self.mActive = True
        return

    def getX(self):
        return self.mX

    def getY(self):
        return self.mY

    def getDX(self):
        return self.mDx

    def getDY(self):
        return self.mDy

    def getWorldWidth(self):
        return self.mWorldWidth

    def getWorldHeight(self):
        return self.mWorldHeight

    def getActive(self):
        return self.mActive

    def setActive(self, input):
        self.mActive = input
        return

    def move(self, dt):
        self.mX += (self.mDx * dt)
        self.mY += (self.mDy * dt)

        if self.mX < 0:
            self.mX = self.mWorldWidth + self.mX
        if self.mY < 0:
            self.mY = self.mWorldHeight + self.mY
        if self.mX >= self.mWorldWidth:
            self.mX = (self.mX - self.mWorldWidth) + 0
        if self.mY >= self.mWorldHeight:
            self.mY = (self.mY - self.mWorldHeight) + 0

        return

    def accelerate(self, uh):
        raise NotImplementedError

    def evolve(self, uh):
        raise NotImplementedError

    def draw(self, surface):
        raise NotImplementedError

    def getRadius(self):
        raise NotImplementedError

    def hits(self, obj2):
        reee = False
        x1 = self.mX
        y1 = self.mY
        r1 = self.getRadius()
        x2 = obj2.getX()
        y2 = obj2.getY()
        r2 = obj2.getRadius()
        d = math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))
        # print("distance between " + str(d))
        # print("Radius combined " + str(r1 + r2))

        if d <= (r1 + r2):
            reee = True
       #     print(str(reee))
        else:
            reee = False
        #    print(str(reee))
        # print(str(reee))
        return reee


