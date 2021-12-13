import polygon, random, math

class Rock(polygon.Polygon):

    def __init__(self, mX, mY, mWorldWidth, mWorldHeight):
        mRotation = random.randrange(0, 359)
        mSpin = random.uniform(-90, 90)

        polygon.Polygon.__init__(self, mX, mY, 0, 0, mRotation, mWorldWidth, mWorldHeight)
        self.mSpinRate = mSpin
        self.accelerate(random.randint(10, 20))
#        self.setPolygon(random.randint(8, 40))
        self.setPolygon(self.randomPolygon(30, random.randint(5, 10)))

        return


    def randomPolygon(self, radius, points):
        nPtList = []
        theta = 360/points
        for i in range(points):
            r = random.uniform(radius*.7, radius*.3)
            x = r* math.cos(math.radians(theta*i))
            y = r* math.sin(math.radians(theta*i))
            nPtList.append((x,y))
        return nPtList

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

    def getSpinRate(self):
        return self.mSpinRate

    def setSpinRate(self, num):
        self.mSpinRate = num
        return

    def createRandomPolygon(self, radius, num):
         rList = []
         n = num

         for i in range(n):
             theta = (i*360)/n
             thetaR = math.radians(theta)
             r = (random.random() * .6 + .7) * radius
             x = math.cos(thetaR) * r
             y = math.sin(thetaR) * r
             rList.append((x, y))

         return rList

    def evolve(self, dt):
        self.move(dt)
        self.rotate((self.mSpinRate*dt))
        return
