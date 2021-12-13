import polygon, pygame, bullet

class Ship(polygon.Polygon):

    def __init__(self, X, Y, mWorldWidth, mWorldHeight):
        polygon.Polygon.__init__(self, X, Y, 0, 0, 0, mWorldWidth, mWorldHeight)
        self.setPolygon([(10, 0), (-10, -10), (-5, 0), (-10, 10)])
        # self.setColor((0, 255, 0))
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

    def evolve(self, dt):
        self.move(dt)
        return

    def fire(self):

        list = self.getPolygon()
        point = list[0]
        xY = self.rotateAndTranslatePoint(point[0], point[1])
        bang = bullet.Bullet(xY[0], xY[1], self.mDx, self.mDy, self.mRotation, self.mWorldWidth, self.mWorldHeight)
        return bang
