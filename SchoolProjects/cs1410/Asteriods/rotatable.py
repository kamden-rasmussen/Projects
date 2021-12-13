import movable, math


class Rotatable(movable.Movable):

    def __init__(self, mX, mY, mDx, mDy, mRotation, mWorldWidth, mWorldHeight):

        movable.Movable.__init__(self, mX, mY, mDx, mDy, mWorldWidth, mWorldHeight)
        self.mRotation = mRotation

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

    def getRotation(self):
        return self.mRotation

    def rotate(self, delta_rotation):

        self.mRotation = (360 + (self.mRotation+delta_rotation) ) % 360

       # pR = delta_rotation + self.mRotation

        #if pR >= 360:
        #    self.mRotation = int(pR - 360)
        #elif pR < 0:
        #    self.mRotation = int(360 - abs(pR))
        #else:
        #    self.mRotation = int(pR)



        return

    def splitDeltaVIntoXAndY(self, rotation, deltaVelocity):
        x = deltaVelocity * math.cos(math.radians(rotation))
        y = deltaVelocity * math.sin(math.radians(rotation))

        return x, y

    def accelerate(self, deltaVelocity):

        returns = self.splitDeltaVIntoXAndY(self.mRotation, deltaVelocity)
        self.mDx += returns[0]
        self.mDy += returns[1]

        return

    def rotatePoint(self, x, y):
        r = math.sqrt((x * x) + (y * y))
        angl = math.atan2(y, x)
        anglP = angl + math.radians(self.mRotation)
        x = r * math.cos(anglP)
        y = r * math.sin(anglP)

        return x, y

    def translatePoint(self, x, y):
        nX = self.mX + x
        nY = self.mY + y

        return nX, nY

    def rotateAndTranslatePoint(self, x, y):
        rotation = self.rotatePoint(x, y)
        nX = rotation[0]
        nY = rotation[1]
        translation = self.translatePoint(nX, nY)

        return translation[0], translation[1]

    def rotateAndTranslatePointList(self, list):
        nList = []
        for x in list:
            i = self.rotateAndTranslatePoint(x[0], x[1])
            nList.append(i)
        return nList

