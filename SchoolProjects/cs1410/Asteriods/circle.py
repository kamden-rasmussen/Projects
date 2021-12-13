import rotatable, pygame

class Circle (rotatable.Rotatable):

    def __init__(self, mX, mY, mDx, mDy, mRotation, mRadius, mWorldWidth, mWorldHeight):

        rotatable.Rotatable.__init__(self, mX, mY, mDx, mDy, mRotation, mWorldWidth, mWorldHeight)
        self.mRadius = mRadius
        self.mColor = (255, 255, 255)

        return

    def getColor(self):
        return self.mColor

    def getRadius(self):
        return self.mRadius

    def setRadius(self, value):
        if value >= 1:
            self.mRadius = value
        return

    def setColor(self, nColor):
           self.mColor = nColor
           return

    def draw(self, surface):
        pygame.draw.circle(surface, self.mColor, (self.mX, self.mY), self.mRadius)
        return
