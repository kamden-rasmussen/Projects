import rotatable, math, pygame

class Polygon(rotatable.Rotatable):

    def __init__(self, mX, mY, mDx, mDy, mRotation, mWorldWidth, mWorldHeight):

        rotatable.Rotatable.__init__(self, mX, mY, mDx, mDy, mRotation, mWorldWidth, mWorldHeight)

        self.mPolygon = []
        self.mColor = (255, 255, 255)

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

    def getPolygon(self):
        return self.mPolygon

    def getColor(self):
        return self.mColor

    def setPolygon(self, list):
        self.mPolygon = list
        return

    def setColor(self, color):
        self.mColor = color
        return

    def draw(self, surface):

        points = self.getPolygon()
        listOfPoints = self.rotateAndTranslatePointList(points)
        pygame.draw.polygon(surface, self.mColor, listOfPoints, 2)

        return

    def getRadius(self):
        avgDis = 0
        listOfLengths = []
        numOfPoints = 0
        sumOfPoints = 0

        if self.mPolygon == []:
            return avgDis
        # [(1,2), (3,4)]

        for points in self.mPolygon:
            numOfPoints += 1
            tempX = points[0]
            tempY = points[1]
            # print(str(tempX))
            # print(str(tempY))

            d = math.sqrt(((tempX - 0) ** 2) + ((tempY - 0) ** 2))
            listOfLengths.append(d)
            sumOfPoints += d
            # print(str("list of lengths" + str(listOfLengths)))

        # print('final list of lengths ' + str(listOfLengths))
        # print('Final len of list of lengths ' + str(len(listOfLengths)))
        avgDis = float(sumOfPoints / numOfPoints)
        # print(str(avgDis))

        return avgDis










